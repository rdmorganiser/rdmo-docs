# Django-allauth

RDMO uses the excellent [django-allauth](http://www.intenct.nl/projects/django-allauth) as its main authorization library. It enables workflows for user registration and password retrieval, as well as authentication from 3rd party sites using OAUTH2.

The library should be installed in RDMO using:

```bash
pip install rdmo[allauth]
```

## Accounts

To enable regular accounts in RDMO add:

```python
ACCOUNT = True
ACCOUNT_SIGNUP = True
ACCOUNT_TERMS_OF_USE = False

INSTALLED_APPS += [
    'allauth',
    'allauth.account',
]

AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')
MIDDLEWARE.append('allauth.account.middleware.AccountMiddleware')
```

to your `config/settings/local.py`. The setting `ACCOUNT = True` enables the general django-allauth features in RDMO, while `ACCOUNT_SIGNUP = True` enables new users to register with your RDMO instance. `ACCOUNT_TERMS_OF_USE = False` disables the Terms of Use. If you set it to `True` every registering user will have to agree to your policy. The last lines enable django-allauth to be used by RDMO.

The behavior of `django-allauth` can be further configured by the settings documented in the [django-allauth documentation](https://django-allauth.readthedocs.io/en/latest/#contents). RDMO sets some defaults, which can be found in [rdmo/rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/settings.py) in the `rdmo` package.

## Social accounts

In order to use 3rd party accounts (facebook, github, etc.) with RDMO add:

```python
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
MIDDLEWARE.append('allauth.account.middleware.AccountMiddleware')
```

to your `config/settings/local.py`. The setting `SOCIALACCOUNT = True` is used by RDMO to show certain parts of the user interface connected to 3rd party accounts, while as before, the lines after `INSTALLED_APPS` enable the feature to be used by RDMO. `SOCIALACCOUNT_AUTO_SIGNUP = True` forces new users to fill out a signup form even if the provider does provide the email address. Each provider has a separate app you need to add to `INSTALLED_APPS`. A list of all providers supported by django-allauth can be found [here](http://django-allauth.readthedocs.io/en/latest/providers.html).

Once the installation is complete, the credentials of your OAUTH provider need to be entered in the admin interface. This is covered in the [administration chapter](../../administration/allauth.html) of this documentation.


### Keycloak as a socialaccount provider

A [keycloak](https://www.keycloak.org/) instance can be enabled as a [socialaccount provider](https://django-allauth.readthedocs.io/en/latest/socialaccount/providers/keycloak.html) via `django-allauth`. The main motivation for using this is that it enables the option to login with the institutional [DFN-AAI](https://doku.tid.dfn.de/de:dfnaai:start) Identity Providers and another 3rd party provider (such as ORCID) at the same time in RDMO. Information about the setup and configuration of a keycloak instance can be found in [Keycloack guides](https://www.keycloak.org/guides#getting-started). The instance can be configured with a realm specific for RDMO.

In addition to the settings for Social accounts above, a few extra settings are required in the `config/settings/local.py` for keycloak:

```py
SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "APPS": [
            {
                "provider_id": "keycloak",
                "name": "Keycloak",
                "client_id": "<insert-id>",
                "secret": "<insert-secret>",
                "settings": {
                    "server_url": "http://keycloak:8080/realms/master/.well-known/openid-configuration",
                },
            }
        ]
    }
}
INSTALLED_APPS += [
    'allauth.socialaccount.providers.openid_connect',
]
```
