#!/usr/bin/env python3
"""Generate the RDMO settings reference from rdmo.core.settings.

Run ``make settings`` after changing the defaults in the sibling ``rdmo``
checkout.  Use ``make check-settings`` in CI to ensure the committed
reference is current.
"""

from __future__ import annotations

import argparse
import ast
import difflib
from pathlib import Path
import re

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SETTINGS = REPOSITORY_ROOT.parent / "rdmo" / "rdmo" / "core" / "settings.py"
DEFAULT_OUTPUT = REPOSITORY_ROOT / "docs" / "configuration" / "settings.md"
DEFAULT_METADATA = REPOSITORY_ROOT / "docs" / "configuration" / "settings.toml"
DEFAULT_PYPROJECT = REPOSITORY_ROOT.parent / "rdmo" / "pyproject.toml"

SOURCES = {
    "Django": "https://docs.djangoproject.com/en/stable/ref/settings/",
    "django-allauth": "https://docs.allauth.org/en/latest/account/configuration.html",
    "Django REST framework": "https://www.django-rest-framework.org/api-guide/settings/",
    "drf-spectacular": "https://drf-spectacular.readthedocs.io/en/latest/settings.html",
    "django-compressor": "https://django-compressor.readthedocs.io/en/stable/settings/",
    "django-settings-export": "https://github.com/ryanhiebert/django-settings-export",
    "RDMO": "https://github.com/rdmorganiser/rdmo/blob/main/rdmo/core/settings.py",
}
RDMO_CODE_SEARCH = "https://github.com/rdmorganiser/rdmo/search?type=code&q="

DJANGO_SETTINGS = frozenset({
    "AUTHENTICATION_BACKENDS", "CACHES", "DATABASES", "DEBUG", "DEFAULT_AUTO_FIELD", "DEFAULT_FROM_EMAIL",
    "EMAIL_BACKEND", "INSTALLED_APPS", "LANGUAGES", "LANGUAGE_CODE", "LOGIN_REDIRECT_URL", "LOGIN_URL",
    "LOGOUT_URL", "MEDIA_URL", "MESSAGE_STORAGE", "MIDDLEWARE", "ROOT_URLCONF", "SITE_ID", "STATICFILES_FINDERS",
    "STATIC_URL", "STORAGES", "TEMPLATES", "TIME_ZONE", "USE_I18N", "USE_TZ", "WSGI_APPLICATION",
})


def setting_source(name: str) -> str:
    """Return the project that defines the setting's configuration interface."""
    if name in DJANGO_SETTINGS:
        return "Django"
    if name.startswith(("ACCOUNT_", "SOCIALACCOUNT_")):
        return "django-allauth"
    if name == "REST_FRAMEWORK":
        return "Django REST framework"
    if name == "SPECTACULAR_SETTINGS":
        return "drf-spectacular"
    if name == "COMPRESS_PRECOMPILERS":
        return "django-compressor"
    if name == "SETTINGS_EXPORT":
        return "django-settings-export"
    return "RDMO"


def django_docs_version(pyproject: Path) -> str:
    """Read the supported Django minor version from RDMO's dependency range."""
    match = re.search(r'"django>=(\d+\.\d+)(?:\.\d+)?,<', pyproject.read_text())
    if not match:
        raise ValueError(f"could not determine Django version from {pyproject}")
    return match.group(1)


def source_url(source_name: str, name: str, django_version: str) -> str:
    """Return the most specific stable upstream reference available."""
    if source_name == "Django":
        return f"https://docs.djangoproject.com/en/{django_version}/ref/settings/#{name.lower().replace('_', '-')}"
    if source_name == "django-allauth" and name.startswith("SOCIALACCOUNT_"):
        return "https://docs.allauth.org/en/latest/socialaccount/configuration.html"
    return SOURCES[source_name]


def infer_type(value: ast.expr) -> str:
    if isinstance(value, ast.Constant):
        return {bool: "bool", int: "int", float: "float", str: "str", type(None): "None"}.get(type(value.value), "object")
    if isinstance(value, (ast.List, ast.ListComp)):
        return "list"
    if isinstance(value, (ast.Tuple, ast.GeneratorExp)):
        return "tuple"
    if isinstance(value, ast.Dict):
        return "dict"
    return "Python expression"


def load_metadata(path: Path) -> dict[str, dict[str, object]]:
    if not path.is_file():
        return {}
    return tomllib.loads(path.read_text()).get("settings", {})


def iter_settings(source: str) -> list[tuple[str, str, str]]:
    """Return uppercase module assignments and their Python representations."""
    settings = []
    for node in ast.parse(source).body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if len(targets) != 1 or not isinstance(targets[0], ast.Name):
                continue
            name = targets[0].id
            if name.isupper() and node.value is not None:
                settings.append((name, ast.get_source_segment(source, node.value) or ast.unparse(node.value), infer_type(node.value)))
    return settings


def render(settings: list[tuple[str, str, str]], source: Path, metadata: dict[str, dict[str, object]], django_version: str) -> str:
    lines = [
        "# Settings",
        "",
        "This reference is generated from the default settings in "
        "[`rdmo/core/settings.py`](https://github.com/rdmorganiser/rdmo/blob/main/rdmo/core/settings.py). "
        "It lists every uppercase setting defined by RDMO and its default value.",
        "",
        "The **Source** field identifies the project that defines a setting's configuration interface. "
        "RDMO-owned settings are implemented or consumed by RDMO; third-party and Django settings retain "
        "their upstream behaviour.",
        "",
        "Set overrides in `config/settings/local.py`; see the [configuration overview](./index) "
        "and the linked topic guides for deployment advice and examples.",
        "",
        "For example, import and extend collection settings rather than replacing the defaults:",
        "",
        "```python",
        "from . import ALLOWED_HOSTS, INSTALLED_APPS",
        "",
        "ALLOWED_HOSTS = ['rdmo.example.org']",
        "INSTALLED_APPS += ['rdmo_theme']",
        "```",
        "",
        "> Do not edit this file by hand. Regenerate it with `make settings` after changing "
        f"[{source.name}](https://github.com/rdmorganiser/rdmo/blob/main/rdmo/core/settings.py).",
        "",
        f"RDMO currently defines **{len(settings)} settings**.",
        "",
    ]
    for name, value, inferred_type in settings:
        if name == "ACCOUNT":
            lines.extend((
                "## RDMO account and social-account integration",
                "",
                "RDMO integrates with django-allauth and uses several `ACCOUNT_*` and `SOCIALACCOUNT_*` "
                "settings of its own. RDMO-specific settings are consumed by RDMO adapters and middleware; "
                "they are not necessarily recognised by a standalone django-allauth installation.",
                "",
            ))
        definition = metadata.get(name, {})
        source_name = str(definition.get("source", setting_source(name)))
        setting_type = str(definition.get("type", inferred_type))
        description = str(definition.get("description", ""))
        lines.extend((f"## {name}", "", f"**Source:** [{source_name}]({source_url(source_name, name, django_version)})", ""))
        lines.extend((f"**Type:** `{setting_type}`", ""))
        if description:
            lines.extend((description, ""))
        if source_name == "RDMO":
            lines.extend((f"**Used in:** [GitHub code search]({RDMO_CODE_SEARCH}{name})", ""))
        related = definition.get("related_settings", [])
        if related:
            links = ", ".join(f"[{item}](#{str(item).lower()})" for item in related)
            lines.extend((f"**Related settings:** {links}", ""))
        interaction = definition.get("interaction")
        if interaction:
            lines.extend((f"**Interaction:** {interaction}", ""))
        lines.extend(("Default:", "", "```python", value, "```", ""))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--settings", type=Path, default=DEFAULT_SETTINGS, help="path to rdmo/core/settings.py")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="reference file to generate")
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA, help="TOML setting definitions")
    parser.add_argument("--pyproject", type=Path, default=DEFAULT_PYPROJECT, help="path to RDMO pyproject.toml")
    parser.add_argument("--check", action="store_true", help="fail when the output is not current")
    parser.add_argument("--stdout", action="store_true", help="write the generated reference to standard output")
    args = parser.parse_args()

    if not args.settings.is_file():
        parser.error(f"settings file does not exist: {args.settings}")

    generated = render(
        iter_settings(args.settings.read_text()), args.settings, load_metadata(args.metadata), django_docs_version(args.pyproject)
    )
    if args.stdout:
        print(generated, end="")
        return 0
    current = args.output.read_text() if args.output.exists() else ""
    if args.check:
        if generated == current:
            return 0
        print(f"{args.output} is out of date; run make settings.")
        print("".join(difflib.unified_diff(current.splitlines(True), generated.splitlines(True), fromfile=str(args.output), tofile="generated")))
        return 1

    args.output.write_text(generated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
