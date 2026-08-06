#!/usr/bin/env python3
"""One-off migration of the former hand-written settings descriptions to TOML."""

import re
import subprocess
from pathlib import Path

from generate_settings_reference import DEFAULT_METADATA, DEFAULT_SETTINGS, iter_settings, setting_source


def description(section: str) -> str:
    lines = section.strip().splitlines()
    if not lines or not lines[0].startswith("Default"):
        return ""
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines) and lines[index].startswith("```"):
        index += 1
        while index < len(lines) and not lines[index].startswith("```"):
            index += 1
        index += 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    return "\n".join(lines[index:]).strip()


def quote(value: str) -> str:
    return "'''" + value.replace("'''", "\\'\\'\\'") + "'''"


def main() -> None:
    legacy = subprocess.run(
        ["git", "show", "HEAD:docs/configuration/settings.md"], capture_output=True, text=True, check=True
    ).stdout
    legacy_descriptions = {
        match.group(1): description(match.group(2))
        for match in re.finditer(r"^### ([A-Z][A-Z0-9_]+)\n(.*?)(?=^### |\Z)", legacy, re.MULTILINE | re.DOTALL)
    }
    lines = [
        "# Human-maintained documentation metadata for rdmo/core/settings.py.",
        "# Defaults and ordering are deliberately extracted from the RDMO source.",
        "",
    ]
    for name, _, setting_type in iter_settings(DEFAULT_SETTINGS.read_text()):
        lines.extend((f"[settings.{name}]", f'source = "{setting_source(name)}"', f'type = "{setting_type}"'))
        if text := legacy_descriptions.get(name):
            lines.append(f"description = {quote(text)}")
        else:
            lines.append('description = ""')
        lines.append("")
    DEFAULT_METADATA.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
