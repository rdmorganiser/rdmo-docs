# Settings

RDMO can be customised using various settings. Since RDMO is based on Django, we use its [build-in settings system](https://docs.djangoproject.com/en/stable/topics/settings/). Almost every setting has a default value, which is set in the RDMO packacge in [rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/main/rdmo/core/settings.py).

In the following all settings, which can be changed from their default values to customize you particular RDMO instance are described in detail.

---

### DEBUG

Default: `False`

Debug mode. When enabled, this provides detailed error messages and debugging information, which is useful during development but should never be enabled in production environments due to security risks.

See also [DEBUG](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEBUG) in the Django documentation.

### ALLOWED_HOSTS

Default: `[]`

List of allowed hosts for this app. If your instance runs under `https://rdmo.example.com` the list needs to contain `rdmo.example.com`.

This setting is used for security purposes to prevent HTTP Host header attacks. It should contain the domain names or IP addresses that are allowed to serve your application.

See also [ALLOWED_HOSTS](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-ALLOWED_HOSTS) in the Django documentation.

### INSTALLED_APPS

The list of Django apps for this RDMO instance. By default, it contains the main Django apps, the RDMO apps from the RDMO package and some 3rd party packages. A theme and or plugins need to be added to this list when used, e.g.:

```python
from . import INSTALLED_APPS
INSTALLED_APPS += ['rdmo_theme', 'rdmo_plugin']
```

See also [INSTALLED_APPS](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-INSTALLED_APPS) in the Django documentation.

## Authentication Settings

### AUTHENTICATION_BACKENDS

Default:

```python
[
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend'
]
```

Authentication backends control how users are authenticated. The default configuration includes both the RDMO-specific object permission backend and Django's standard model backend.

### MULTISITE

Default: `False`

Controls whether the RDMO instance supports multiple sites. When enabled, it allows for different configurations and content for different domains.

### GROUPS

Default: `False`

Enables or disables group-based permissions and management features in RDMO.

### LOGIN_FORM

Default: `True`

Controls whether the login form is displayed on the site.

### PROFILE_UPDATE

Default: `True`

Enables or disables the ability for users to update their profile information.

### PROFILE_DELETE

Default: `True`

Enables or disables the ability for users to delete their profiles.

### ACCOUNT

Default: `False`

Enables or disables the account management system.

### ACCOUNT_SIGNUP

Default: `False`

Enables or disables user signup functionality.

### ACCOUNT_GROUPS

Default: `[]`

Defines groups that users can be assigned to during signup.

### ACCOUNT_TERMS_OF_USE

Default: `False`

Enables or disables terms of use acceptance during signup.

### ACCOUNT_ACTIVATION_DAYS

Default: `7`

Number of days after which account activation links expire.

### ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS

Default: `7`

Number of days after which email confirmation links expire.

### ACCOUNT_EMAIL_VERIFICATION

Default: `'optional'`

Controls how email verification is handled. Options include `'optional'`, `'mandatory'`, or `'none'`.

### ACCOUNT_USERNAME_MIN_LENGTH

Default: `4`

Minimum length required for usernames.

### ACCOUNT_PASSWORD_MIN_LENGTH

Default: `4`

Minimum length required for passwords.

### ACCOUNT_ALLOW_USER_TOKEN

Default: `False`

Enables or disables user token functionality.

### SOCIALACCOUNT

Default: `False`

Enables or disables social account authentication.

### SOCIALACCOUNT_SIGNUP

Default: `False`

Enables or disables signup via social accounts.

### SOCIALACCOUNT_GROUPS

Default: `[]`

Defines groups that users can be assigned to during social account signup.

## Shibboleth Authentication

### SHIBBOLETH

Default: `False`

Enables or disables Shibboleth authentication.

### SHIBBOLETH_LOGIN_URL

Default: `'/Shibboleth.sso/Login'`

URL to the Shibboleth login endpoint.

### SHIBBOLETH_LOGOUT_URL

Default: `'/Shibboleth.sso/Logout'`

URL to the Shibboleth logout endpoint.

### SHIBBOLETH_USERNAME_PATTERN

Default: `None`

Pattern to extract username from Shibboleth attributes.

## Internationalization Settings

### LANGUAGE_CODE

Default: `'en-us'`

The default language code for the application.

### TIME_ZONE

Default: `'Europe/Berlin'`

The default time zone for the application.

### LANGUAGES

Default:

```python
(
    ('en', _('English')),
    ('de', _('German')),
)
```

List of supported languages for the application.

## Database Settings

### DATABASES

Default:

```
{
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}
```

Database configuration. The default uses SQLite for development, but production environments should use PostgreSQL or MySQL.

## Email Settings

### EMAIL_BACKEND

Default: `'django.core.mail.backends.console.EmailBackend'`

Email backend to use for sending emails. In production, this should be configured to use a real email service.

### DEFAULT_FROM_EMAIL

Default: `'info@example.com'`

Default email address to use for sending emails.

### EMAIL_RECIPIENTS_CHOICES

Default: `[]`

List of email recipients for notifications.

### EMAIL_RECIPIENTS_INPUT

Default: `False`

Controls whether users can specify email recipients when sending notifications.

## Project Settings

### OVERLAYS

Default:

```python
{
    'projects': [
        'projects-table',
        'create-project',OPTIONSET_PROVIDERS
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

Controls which UI elements are displayed in different project contexts.

### EXPORT_FORMATS

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

List of supported export formats for project data.

### EXPORT_REFERENCE_ODT_VIEWS

Default `{}`

### EXPORT_REFERENCE_DOCX_VIEWS

Default `{}`

### EXPORT_REFERENCE_ODT

Default: `None`

### EXPORT_REFERENCE_DOCX

Default: `None`

### EXPORT_PANDOC_ARGS

Default:

```python
{
    'pdf': ['-V', 'geometry:a4paper, margin=1in', '--pdf-engine=xelatex'],
    'rtf': ['--standalone']
}
```

Arguments passed to pandoc when converting documents to different formats.

### EXPORT_CONTENT_DISPOSITION

Default `'attachment'`

Controls how exported files are handled by the browser.

### PROJECT_TABLE_PAGE_SIZE

Default: `20`

Number of projects to display per page in project tables.

### PROJECT_ISSUES

Default: `True`

Enables or disables the issue tracking system for projects.

### PROJECT_ISSUE_PROVIDERS

Default: `[]`

List of issue providers that can be used for project issues.

### PROJECT_VIEWS

Default: `True`

Enables or disables the project views feature.

### PROJECT_EXPORTS

Default:

```python
[
    ('xml', _('RDMO XML'), 'rdmo.projects.exports.RDMOXMLExport'),
    ('csvcomma', _('CSV (comma separated)'), 'rdmo.projects.exports.CSVCommaExport'),
    ('csvsemicolon', _('CSV (semicolon separated)'), 'rdmo.projects.exports.CSVSemicolonExport'),
    ('json', _('JSON'), 'rdmo.projects.exports.JSONExport'),
]
```

List of supported project export formats.

### PROJECT_SNAPSHOT_EXPORTS

Default: `[]`

### PROJECT_IMPORTS

Default: `[]`

```python
[
    ('xml', _('RDMO XML'), 'rdmo.projects.imports.RDMOXMLImport'),
]
```

List of supported project import formats.

### PROJECT_IMPORTS_LIST

Default: `[]`

### PROJECT_QUESTIONS_AUTOSAVE

Default: `True`

Controls whether project question responses are automatically saved while users are filling out forms.

### PROJECT_QUESTIONS_CYCLE_SETS

Default: `False`

Controls whether cycle sets are enabled for project questions.

### PROJECT_FILE_QUOTA

Default: `'10Mb'`

Controls the maximum amount of storage space that can be used by files attached to projects.

### PROJECT_SEND_ISSUE

Default: `False`

Enables or disables sending issues to users.

### PROJECT_INVITE_TIMEOUT

Default: `None`

Timeout for project invitations.

### PROJECT_SEND_INVITE

Default: `True`

Enables or disables sending invitations to users.

### PROJECT_REMOVE_VIEWS

Default: `True`

Enables or disables removal of views from projects.

### PROJECT_CREATE_RESTRICTED

Default: `False`

The `PROJECT_CREATE_RESTRICTED` setting is a boolean flag that controls whether project creation is restricted in an RDMO instance.

### PROJECT_CREATE_GROUPS

Default: `[]`

The `PROJECT_CREATE_GROUPS` setting is used to restrict who can create new projects in an RDMO instance. It's part of a broader project creation restriction system that includes the `PROJECT_CREATE_RESTRICTED` setting.

### PROJECT_VALUES_CONFLICT_THRESHOLD

Default: `0.01`

A time delta in seconds for detecting conflicts in project values in case multiple users edit the same project values simultaneously.

### NESTED_PROJECTS

Default: `True`

Enables or disables nested projects.

### OPTIONSET_PROVIDERS

Default: `[]`

List of option set providers.

## Validation Settings

### PROJECT_VALUES_VALIDATION

Default: `False`

Enables or disables validation of project values.

### PROJECT_VALUES_VALIDATION_URL

Default: `True`

Enables or disables URL validation.

### PROJECT_VALUES_VALIDATION_INTEGER

Default: `True`

Enables or disables integer validation.

### PROJECT_VALUES_VALIDATION_INTEGER_MESSAGE

Default: `_('Enter a valid integer.')`

Error message for integer validation.

### PROJECT_VALUES_VALIDATION_INTEGER_REGEX

Default: `re.compile(r'^[+-]?\d+$')`

Regular expression for integer validation.

### PROJECT_VALUES_VALIDATION_FLOAT

Default: `True`

Enables or disables float validation.

### PROJECT_VALUES_VALIDATION_FLOAT_MESSAGE

Default: `_('Enter a valid float.')`

Error message for float validation.

### PROJECT_VALUES_VALIDATION_FLOAT_REGEX

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

Regular expression for float validation.

### PROJECT_VALUES_VALIDATION_BOOLEAN

Default: `True`

Enables or disables boolean validation.

### PROJECT_VALUES_VALIDATION_BOOLEAN_MESSAGE

Default: `_('Enter a valid boolean (e.g. 0, 1).')`

Error message for boolean validation.

### PROJECT_VALUES_VALIDATION_BOOLEAN_REGEX

Default: `r'(?i)^(0|1|f|t|false|true)$'`

Regular expression for boolean validation.

### PROJECT_VALUES_VALIDATION_DATE

Default: `True`

Enables or disables date validation.

### PROJECT_VALUES_VALIDATION_DATE_MESSAGE

Default: `_('Enter a valid date (e.g. "02.03.2024", "03/02/2024", "2024-02-03").')`

Error message for date validation.

### PROJECT_VALUES_VALIDATION_DATE_REGEX

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

Regular expression for date validation.

### PROJECT_VALUES_VALIDATION_DATETIME

Default: `True`

Enables or disables datetime validation.

### PROJECT_VALUES_VALIDATION_EMAIL

Default: `True`

Enables or disables email validation.

### PROJECT_VALUES_VALIDATION_PHONE

Default: `True`

Enables or disables phone number validation.

### PROJECT_VALUES_VALIDATION_PHONE_MESSAGE

Default: `_('Enter a valid phone number (e.g. "123456" or "+49 (0) 30 123456").')`

Error message for phone number validation.

### PROJECT_VALUES_VALIDATION_PHONE_REGEX

Default:

```python
re.compile(r'''
    ^([+]\d{2,3}\s)?  # Optional country code
    (\(\d+\)\s)?      # Optional area code in parentheses
    [\d\s]*$          # Main number with spaces
''', re.VERBOSE)
```

Regular expression for phone number validation.

## Other Settings

### DEFAULT_URI_PREFIX

Default: `'http://example.com/terms'`

Default URI prefix used for terms and conditions.

### REPLACE_MISSING_TRANSLATION

Default: `False`

Controls whether missing translations should be replaced with the default language version.
