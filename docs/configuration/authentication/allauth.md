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

The behavior of `django-allauth` can be further configured by the settings documented in the [django-allauth documentation](https://django-allauth.readthedocs.io/en/latest/#contents). RDMO sets some defaults, which can be found in [rdmo/rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/main/rdmo/core/settings.py) in the `rdmo` package.

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

to your `config/settings/local.py`. The setting `SOCIALACCOUNT = True` is used by RDMO to show certain parts of the user interface connected to 3rd party accounts, while as before, the lines after `INSTALLED_APPS` enable the feature to be used by RDMO. `SOCIALACCOUNT_AUTO_SIGNUP = True` forces new users to fill out a signup form even if the provider does provide the email address. Each provider has a separate app you need to add to `INSTALLED_APPS`. A list of all providers supported by django-allauth can be found [here](https://docs.allauth.org/en/latest/socialaccount/providers/index.html).

Once the installation is complete, the credentials of your OAUTH provider need to be entered in the admin interface. This is covered in the [administration chapter](../../administration/allauth) of this documentation.


## Other 3rd party authentication solutions

### Generic OpenID Connect provider

The generic `openid_connect` provider from `django-allauth` allows for an easy configuration of multiple OpenID Connect providers. 

In addition to the settings for Social accounts above, a few extra settings are required in the `config/settings/local.py` for this provider. Please note the [django-allauth docs on openid-connect](https://docs.allauth.org/en/latest/socialaccount/providers/openid_connect.html#openid-connect) for the source of the following information: 
```py
SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "APPS": [
            {
                "provider_id": "my-server",
                "name": "My Login Server",
                "client_id": "your.service.id",
                "secret": "your.service.secret",
                "settings": {
                    "server_url": "https://my.server.example.com",
                    # Optional token endpoint authentication method.
                    # May be one of "client_secret_basic", "client_secret_post"
                    # If omitted, a method from the the server's
                    # token auth methods list is used
                    "token_auth_method": "client_secret_basic",
                },
            },
            {
                "provider_id": "other-server",
                "name": "Other Login Server",
                "client_id": "your.other.service.id",
                "secret": "your.other.service.secret",
                "settings": {
                    "server_url": "https://other.server.example.com",
                },
            },
        ]
    }
}
```
and add the provider to `INSTALLED_APPS`
```py
INSTALLED_APPS += [
    'allauth.socialaccount.providers.openid_connect',
]
```

The **OpenID Connect** callback URL for each configured server will use the  `provider_id` as the `{id}` in `accounts/{id}/login/callback/`.

### Keycloak as a socialaccount provider

A [keycloak](https://www.keycloak.org/) instance can be enabled as a generic `openid_connect` 
 [socialaccount provider](https://docs.allauth.org/en/latest/socialaccount/providers/keycloak.html) via `django-allauth`. The main motivation for using this is that it enables the option to login with the institutional [DFN-AAI](https://doku.tid.dfn.de/de:dfnaai:start) Identity Providers (SAML) and another 3rd party provider (OIDC, such as ORCID) at the same time in RDMO. Information about the setup and configuration of a keycloak instance can be found in [Keycloack guides](https://www.keycloak.org/guides#getting-started). The instance can be configured with a realm specific for RDMO.


### NFDI-AAI Community AAI solutions

For RDMO service providers that are related to a NFDI Consortium, there might be the possibility to join a Community AAI solution in the context of the [NFDI-AAI](http://nfdi-aai.de/) project. These Identity Providers support both SAML and OIDC, where the OIDC can be readily configured in RDMO via the [generic `openid_connect` provider](#generic-openid-connect-provider) from `django-allauth`.

### SAML supported by socialaccount provider

Recently, a SAML provider app has been implemented in `django-allauth` as well. This allows one to configure and enable a SAML and OIDC Identity Providers in parallel from within the RDMO deployment. However, so far, this feature has not been tested in the RDMO Community. Please find the [django-allauth docs on SAML](https://docs.allauth.org/en/latest/socialaccount/providers/saml.html#saml) for more information.
