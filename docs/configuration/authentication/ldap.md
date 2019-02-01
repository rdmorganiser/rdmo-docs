# LDAP

In order to use a LDAP backend with RDMO you need to install some prerequistes. On Debian/Ubuntu you can install them using:

```bash
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```

On the python side, we use [django-auth-ldap](https://pypi.org/project/django-auth-ldap) to connect to the LDAP server. As before, it should be installed inside the virtual environment created for RDMO using:

```bash
pip install -r requirements/ldap.txt
```

LDAP installations can be very different and we only discuss one particular example. We assume that the LDAP service is running on `ldap.example.com`. RDMO needs a *System Account*. In order to create it, run:

```bash
ldapmodify -x -D 'cn=Directory Manager' -W
```

on the machine running the LDAP service and type in:

```
dn: uid=system,cn=sysaccounts,cn=etc,dc=example,dc=com
changetype: add
objectclass: account
objectclass: simplesecurityobject
uid: rdmo
userPassword: YOURPASSWORD
passwordExpirationTime: 20380119031407Z
nsIdleTimeout: 0
```

and end with a blank line followed by `ctrl-d`.

Then, in your `config/settings/local.py` add or uncomment:

```python
import ldap
from django_auth_ldap.config import LDAPSearch
from rdmo.core.settings import AUTHENTICATION_BACKENDS

PROFILE_UPDATE = False
PROFILE_DELETE = False

AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
AUTH_LDAP_BIND_DN = "cn=rdmo,dc=ldap,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "YOURPASSWORD"
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=ldap,dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    'email': 'mail'
}

AUTHENTICATION_BACKENDS.insert(
    AUTHENTICATION_BACKENDS.index('django.contrib.auth.backends.ModelBackend'),
    'django_auth_ldap.backend.LDAPBackend'
)
```

The setting `PROFILE_UPDATE = False` and `PROFILE_DELETE = False` tell RDMO to disable the update and deletion form for the user profile so that users can neither update their credentials nor delete their profile anymore. The other settings are needed by `django-auth-ldap` and are described in the [django-auth-ldap documentation](https://pypi.org/project/django-auth-ldap).
