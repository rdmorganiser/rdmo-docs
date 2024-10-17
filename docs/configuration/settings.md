Settings
========

RDMO can be customised using various settings. Since RDMO is based on Django, we use its [build-in settings system](https://docs.djangoproject.com/en/stable/topics/settings/). Almost every setting has a default value, which is set in the RDMO packacge in [rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/main/rdmo/core/settings.py).

In the following all settings, which can be changed from their default values to customize you particular RDMO instance are described in detail.

---

#### SECRET_KEY

Secret key for RDMO. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value (e.g. from a password generator).

See also [SECRET_KEY](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY) in the Django documentation. Should be set in `.env`.

---

#### DEBUG

Default: `False`

Debug mode. See also [DEBUG](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEBUG) in the Django documentation. Should **never** set to `True` in production.

---

#### ALLOWED_HOSTS

Default: `[]`

List of allowed hosts for this app. If your instance runs under `https://rdmo.example.com` the list needs to contain `rdmo.example.com`.

See also [ALLOWED_HOSTS](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-ALLOWED_HOSTS) in the Django documentation.

---

#### INSTALLED_APPS

The list of Django apps for this RDMO instance. By default, it contains the main Django apps, the RDMO apps from the RDMO package and some 3rd party packages. A theme and or plugins need to be added to this list when used, e.g.:

```python
from . import INSTALLED_APPS 
INSTALLED_APPS += ['rdmo_theme', 'rdmo_plugin']
```

See also [INSTALLED_APPS](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-INSTALLED_APPS) in the Django documentation.

---

#### AUTHENTICATION_BACKENDS

Default:

```python
[
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend'
]
```

---

#### MULTISITE

Default: `False`

---

#### GROUPS

Default: `False`

---

#### LOGIN_FORM

Default: `True`

---

#### PROFILE_UPDATE

Default: `True`

---

#### PROFILE_DELETE

Default: `True`

---

#### ACCOUNT

Default: `False`

---

#### ACCOUNT_SIGNUP

Default: `False`

---

#### ACCOUNT_GROUPS

Default: `[]`

---

#### ACCOUNT_TERMS_OF_USE

Default: `False`

---

#### ACCOUNT_ACTIVATION_DAYS

Default: `7`

---

#### ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS

Default: `7`

---

#### ACCOUNT_EMAIL_VERIFICATION

Default: `'optional'`

---

#### ACCOUNT_USERNAME_MIN_LENGTH 

Default: `4`

---

#### ACCOUNT_PASSWORD_MIN_LENGTH

Default: `4`

---

#### ACCOUNT_ALLOW_USER_TOKEN

Default: `False`

---

#### SOCIALACCOUNT

Default: `False`

---

#### SOCIALACCOUNT_SIGNUP

Default: `False`

---

#### SOCIALACCOUNT_GROUPS

Default: `[]`

---

#### SHIBBOLETH

Default: `False`

---

#### SHIBBOLETH_LOGIN_URL

Default: `'/Shibboleth.sso/Login'`

---

#### SHIBBOLETH_LOGOUT_URL

Default: `'/Shibboleth.sso/Logout'`

---

#### SHIBBOLETH_USERNAME_PATTERN

Default: `None`

---

#### LANGUAGE_CODE

Default: `'en-us'`

---

#### TIME_ZONE

Default: `'Europe/Berlin'`

---

#### LANGUAGES

Default:

```python
(
    ('en', _('English')),
    ('de', _('German')),
)
```

---

#### DATABASES

Default:

```
{
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}
```

---

#### EMAIL_BACKEND

Default: `'django.core.mail.backends.console.EmailBackend'`

---

#### DEFAULT_FROM_EMAIL

Default: `'info@example.com'`

---

#### EMAIL_RECIPIENTS_CHOICES

Default: `[]`

---

#### EMAIL_RECIPIENTS_INPUT

Default: `False`

---

#### USER_API

Default: `True`

---

#### OVERLAYS 

Default: 

```python
{
    'projects': [
        'projects-table',
        'create-project',
        'import-project',
        'support-info'
    ],
    'project': [
        'project-questions',
        'project-catalog',
        'project-issues',
        'project-views',
        'project-memberships',
        'project-snapshots',
        'export-project',
        'import-project',
        'support-info'
    ],
    'issue_send': [
        'issue-message',
        'issue-attachments',
        'support-info'
    ]
}
```

---

#### EXPORT_FORMATS 

Default:

```python
(
    ('pdf', _('PDF')),
    ('rtf', _('Rich Text Format')),
    ('odt', _('Open Office')),
    ('docx', _('Microsoft Office')),
    ('html', _('HTML')),
    ('markdown', _('Markdown')),
    ('mediawiki', _('mediawiki')),
    ('tex', _('LaTeX'))
)
```

---

#### EXPORT_REFERENCE_ODT_VIEWS 

Default `{}`

---

#### EXPORT_REFERENCE_DOCX_VIEWS

Default `{}`

---

#### EXPORT_REFERENCE_ODT

Default: `None`

---

#### EXPORT_REFERENCE_DOCX

Default: `None`

---

#### EXPORT_PANDOC_ARGS

Default:

```python
{
    'pdf': ['-V', 'geometry:a4paper, margin=1in', '--pdf-engine=xelatex'],
    'rtf': ['--standalone']
}
```

---

#### EXPORT_CONTENT_DISPOSITION

Default `'attachment'`

---

#### PROJECT_TABLE_PAGE_SIZE

Default: `20`

---

#### PROJECT_ISSUES

Default: `True`

---

#### PROJECT_ISSUE_PROVIDERS

Default: `[]`

---

#### PROJECT_VIEWS

Default: `True`

---

#### PROJECT_EXPORTS

Default:

```python
[
    ('xml', _('RDMO XML'), 'rdmo.projects.exports.RDMOXMLExport'),
    ('csvcomma', _('CSV (comma separated)'), 'rdmo.projects.exports.CSVCommaExport'),
    ('csvsemicolon', _('CSV (semicolon separated)'), 'rdmo.projects.exports.CSVSemicolonExport'),
    ('json', _('JSON'), 'rdmo.projects.exports.JSONExport'),
]
```

---

#### PROJECT_SNAPSHOT_EXPORTS 

Default: `[]`

---

#### PROJECT_IMPORTS

Default: `[]`

```python
[
    ('xml', _('RDMO XML'), 'rdmo.projects.imports.RDMOXMLImport'),
]
```

---

#### PROJECT_IMPORTS_LIST

Default: `[]`

---

#### PROJECT_QUESTIONS_AUTOSAVE

Default: `True`

---

#### PROJECT_QUESTIONS_CYCLE_SETS

Default: `False`

---

#### PROJECT_FILE_QUOTA

Default: `'10Mb'`

---

#### PROJECT_SEND_ISSUE

Default: `False`

---

#### PROJECT_INVITE_TIMEOUT

Default: `None`

---

#### PROJECT_SEND_INVITE

Default: `True`

---

#### PROJECT_REMOVE_VIEWS 

Default: `True`

---

#### PROJECT_CREATE_RESTRICTED

Default: `False`

---

#### PROJECT_CREATE_GROUPS

Default: `[]`

---

#### PROJECT_VALUES_CONFLICT_THRESHOLD

Default: `0.01`

---

#### NESTED_PROJECTS

Default: `True`

---

#### OPTIONSET_PROVIDERS

Default: `[]`

---

#### PROJECT_VALUES_VALIDATION

Default: `False`

---

#### PROJECT_VALUES_VALIDATION_URL

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_INTEGER

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_INTEGER_MESSAGE

Default: `_('Enter a valid integer.')`

---

#### PROJECT_VALUES_VALIDATION_INTEGER_REGEX

Default: `re.compile(r'^[+-]?\d+$')`

---

#### PROJECT_VALUES_VALIDATION_FLOAT

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_FLOAT_MESSAGE

Default: `_('Enter a valid float.')`

---

#### PROJECT_VALUES_VALIDATION_FLOAT_REGEX

Default:

```python
re.compile(r'''
    ^[+-]?            # Optional sign
    (
        \d+           # Digits before the decimal or thousands separator
        (,\d{3})*     # Optional groups of exactly three digits preceded by a comma (thousands separator)
        (\.\d+)?      # Optional decimal part, a dot followed by one or more digits
        |             # OR
        \d+           # Digits before the decimal or thousands separator
        (\.\d{3})*    # Optional groups of exactly three digits preceded by a dot (thousands separator)
        (,\d+)?       # Optional decimal part, a comma followed by one or more digits
    )
    ([eE][+-]?\d+)?$  # Optional exponent part
''', re.VERBOSE)
```

---

#### PROJECT_VALUES_VALIDATION_BOOLEAN

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_BOOLEAN_MESSAGE

Default: `_('Enter a valid boolean (e.g. 0, 1).')`

---

#### PROJECT_VALUES_VALIDATION_BOOLEAN_REGEX

Default: `r'(?i)^(0|1|f|t|false|true)$'`

---

#### PROJECT_VALUES_VALIDATION_DATE

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_DATE_MESSAGE

Default: `_('Enter a valid date (e.g. "02.03.2024", "03/02/2024", "2024-02-03").')`

---

#### PROJECT_VALUES_VALIDATION_DATE_REGEX

Default:

```python
re.compile(r'''
    ^(
        \d{1,2}\.\s*\d{1,2}\.\s*\d{2,4}  # Format dd.mm.yyyy
        | \d{1,2}/\d{1,2}/\d{4}          # Format mm/dd/yyyy
        | \d{4}-\d{2}-\d{2}              # Format yyyy-mm-dd
    )$
''', re.VERBOSE)
```

---

#### PROJECT_VALUES_VALIDATION_DATETIME

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_EMAIL

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_PHONE

Default: `True`

---

#### PROJECT_VALUES_VALIDATION_PHONE_MESSAGE

Default: `_('Enter a valid phone number (e.g. "123456" or "+49 (0) 30 123456").')`

---

#### PROJECT_VALUES_VALIDATION_PHONE_REGEX

Default:

```python
re.compile(r'''
    ^([+]\d{2,3}\s)?  # Optional country code
    (\(\d+\)\s)?      # Optional area code in parentheses
    [\d\s]*$          # Main number with spaces
''', re.VERBOSE)
```

---

#### DEFAULT_URI_PREFIX

Default: `'http://example.com/terms'`

---

#### REPLACE_MISSING_TRANSLATION

Default: `False`

---