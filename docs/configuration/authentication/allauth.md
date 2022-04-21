# Django-allauth

RDMO uses the excellent [django-allauth](http://www.intenct.nl/projects/django-allauth) as its main authorization library. It enables workflows for user registration and password retrieval, as well as authentication from 3rd party sites using OAUTH2.

## Accounts

To enable regular accounts in RDMO add:

```python
from rdmo.core.settings import INSTALLED_APPS, AUTHENTICATION_BACKENDS

ACCOUNT = True
ACCOUNT_SIGNUP = True
ACCOUNT_TERMS_OF_USE = False

INSTALLED_APPS += [
    'allauth',
    'allauth.account',
]

AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')
```

to your `config/settings/local.py`. The setting `ACCOUNT = True` enables the general django-allauth features in RDMO, while `ACCOUNT_SIGNUP = True` enables new users to register with your RDMO instance. `ACCOUNT_TERMS_OF_USE = False` disables the Terms of Use. If you set it to `True` every registering user will have to agree to your policy. The last lines enable django-allauth to be used by RDMO.

The behavior of `django-allauth` can be further configured by the settings documented in the [django-allauth documentation](http://django-allauth.readthedocs.io/en/latest/configuration.html). RDMO sets some defaults, which can be found in [rdmo/rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/settings.py) in the `rdmo` package.

## Social accounts

In order to use 3rd party accounts (facebook, github, etc.) with RDMO add:

```python
from rdmo.core.settings import INSTALLED_APPS, AUTHENTICATION_BACKENDS

ACCOUNT = True
ACCOUNT_SIGNUP = True
SOCIALACCOUNT = True
SOCIALACCOUNT_SIGNUP = False
SOCIALACCOUNT_AUTO_SIGNUP = False

INSTALLED_APPS += [
    'allauth',
    'allauth.account',
    'allauth.socialaccount'
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.orcid',
    'allauth.socialaccount.providers.twitter',
    ...
]

AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')
```

to your `config/settings/local.py`. The setting `SOCIALACCOUNT = True` is used by RDMO to show certain parts of the user interface connected to 3rd party accounts, while as before, the lines after `INSTALLED_APPS` enable the feature to be used by RDMO. `SOCIALACCOUNT_AUTO_SIGNUP = True` forces new users to fill out a signup form even if the provider does provide the email address. Each provider has a separate app you need to add to `INSTALLED_APPS`. A list of all providers supported by django-allauth can be found [here](http://django-allauth.readthedocs.io/en/latest/providers.html).

Once the installation is complete, the credentials of your OAUTH provider need to be entered in the admin interface. This is covered in the [administration chapter](../../administration/allauth.html) of this documentation.
