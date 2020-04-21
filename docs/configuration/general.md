# General settings

A few general settings should be included in your `config/settings/local.py`. The first, and probably most important one, is if you run RDMO in [debug mode](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-DEBUG) or not:

```python
DEBUG = True
```

In debug mode, verbose error pages are shown in the case something goes wrong and static assets such as CSS and JavaScript files are found by the development server automatically. The debug mode **must not** be enabled when running RDMO in production connected to the internet.

Django needs a [secret key](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY), which "should be set to a unique, unpredictable value":

```python
SECRET_KEY = 'this is not a very secret key'
```

This key must be kept secret since otherwise many of Django’s security protections fail.

In production, Django only [allows requests to certain urls](https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts), which you need to specify:

```python
ALLOWED_HOSTS = ['localhost', 'rdmo.example.com']
```

If you want to run RDMO under an alias like `http://example.com/rdmo`, you need to set the base URL:

```python
BASE_URL = '/rdmo'
```

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

**This needs to be configured before data is imported or content is configured.**

Note that in order to use RDMO with any language a `.po` file needs to be created (see also: https://docs.djangoproject.com/en/stable/topics/i18n/translation/), which contains the translation of all strings in the user interface. RDMO ships with such a file for English and German. Please contact the project if you intend to use RDMO with a new language. Although we will not be able to perform the translation ourselves, we are happy to support you and add the language file to the RDMO source code after review. This translation of stings in the user interface via `gettext` is independent from the  creation/translation from any content (e.g. catalogs, option set), which need to be performed independently through the management interface.

If you run RDMO behind a reverse Proxy, which terminates the TLS/SSL trafic, you need to add the following:

```
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

in order for RDMO to pick up the `X-Forwarded-Host` and `X-Forwarded-Proto` HTTP headers from the proxy.
