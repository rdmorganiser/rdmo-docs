# General settings

A few general settings should be included in your `config/settings/local.py`. The first, and probably most important one, is if you run RDMO in [debug mode](https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-DEBUG) or not:

```python
DEBUG = True
```

In debug mode, verbose error pages are shown in the case something goes wrong and static assets such as CSS and JavaScript files are found by the development server automatically. The debug mode **must not** be enabled when running RDMO in production connected to the internet.

## Secret key
Django needs a [secret key](https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-SECRET_KEY), which "should be set to a unique, unpredictable value":

```python
SECRET_KEY = 'this is not a very secret key'
```
A secret key can be generated with the following command, with your Python environment activated:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

This key must be kept secret since otherwise many of Django’s security protections fail.

## Allowed hosts
As a security measure in production, Django only [allows requests to certain urls](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts). The [fully qualified domain name (FQDN)](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) of your RDMO instance should be added to the settings. Use the following definition to add the FQDN of your RDMO instance to the  `ALLOWED_HOSTS`:

```python
ALLOWED_HOSTS += ['rdmo.example.com']
```

## Language and localization
Furthermore, you might want to choose the main language for RDMO and the timezone:

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
```

By default, RDMO runs with English as the first and German as the second language. It can be configured to run with up to 5 arbitrary languages. For this, the `LANGUAGES` setting need to be added to `config/settings/local.py`. E.g. for French:

```python
from django.utils.translation import ugettext_lazy as _
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
LANGUAGES = (
    ('fr', _('French')),
    ('en', _('English')),
)
```

```{warning}
This needs to be configured **before** any data is imported or content is configured.
```

Note that in order to use RDMO with any language, a `.po` file needs to be created (see also: [django docs on translations](https://docs.djangoproject.com/en/stable/topics/i18n/translation/)). These files contain the translations of all strings in the user interface and can be found in the [RDMO source code](https://github.com/search?q=repo%3Ardmorganiser%2Frdmo+rdmo%2Flocale%2F+django.po&type=code). RDMO ships with translations for English, German, French and Spanish. Please [contact the project](https://github.com/rdmorganiser/rdmo/issues) if you intend to use RDMO with another language, contact information can also be found on the [RDMO community website](https://rdmorganiser.github.io/). Although we will not be able to perform the translation ourselves, we are happy to support you and add the language file to the RDMO source code after review. The `.po` files define the translation of strings in the user web interface via `gettext`. The translation of any of the content items in RDMO (e.g. catalogs, option sets) is independent from these files and is defined separately through the management web interface.

## Optional: Base URL
An **optional** setting, when you want to run RDMO under an alias like `http://example.com/rdmo`, is the `BASE_URL`. When you use an alias you need to set the base URL, otherwise this setting can be ignored.

```python
BASE_URL = '/rdmo'
```
When using this setting, also take into account the configuration under [deployment](../deployment/index).

## Optional: reverse proxy
If you run RDMO behind a reverse Proxy, which terminates the TLS/SSL traffic, you need to add the following:

```
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

in order for RDMO to pick up the `X-Forwarded-Host` and `X-Forwarded-Proto` HTTP headers from the proxy.
