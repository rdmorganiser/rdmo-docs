# LDAP

In order to use a LDAP backend with RDMO you need to install some prerequistes. On Debian/Ubuntu you can install them using:

```bash
sudo apt-get install libsasl2-dev libldap2-dev libssl-dev
```

On the python side, we use [django-auth-ldap](https://pypi.org/project/django-auth-ldap) to connect to the LDAP server. As before, it should be installed inside the virtual environment created for RDMO using:

```bash
pip install -r requirements/ldap.txt
```

LDAP installations can be very different and we only discuss one particular example. We assume that the LDAP service is running on `ldap.example.com`. RDMO needs an account to connect to the LDAP. In order to create it, run:

```bash
ldapmodify -x -D "cn=admin,dc=ldap,dc=example,dc=com" -W
```

on the machine running the LDAP service and type in:

```
dn: uid=rdmo,dc=ldap,dc=example,dc=com
changetype: add
objectclass: account
objectclass: simplesecurityobject
uid: rdmo
userPassword: RDMO_LDAP_ACCOUNT_PASSWORD
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
AUTH_LDAP_BIND_DN = "uid=rdmo,dc=ldap,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "RDMO_LDAP_ACCOUNT_PASSWORD"
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

The connection can be tested using:

```
ldapsearch -v -x -H 'ldap://ldap.example.com' -D "uid=rdmo,dc=ldap,dc=example,dc=com" -w RDMO_LDAP_ACCOUNT_PASSWORD -b "dc=ldap,dc=example,dc=com" -s sub 'uid=user'
```

The setting `PROFILE_UPDATE = False` and `PROFILE_DELETE = False` tell RDMO to disable the update and deletion form for the user profile so that users can neither update their credentials nor delete their profile anymore. The other settings are needed by `django-auth-ldap` and are described in the [django-auth-ldap documentation](https://pypi.org/project/django-auth-ldap).

You can also map LDAP groups to Django groups, in particular to restrict the access to Catalogs and Views. This can be done by adding the following settings:

```
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "dc=ldap,dc=test,dc=rdmo,dc=org", ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
AUTH_LDAP_MIRROR_GROUPS = ['special']
```

where `cn` is the name of the particular group in the LDAP and `AUTH_LDAP_MIRROR_GROUPS` denotes the groups which are actually mirrored from the LDAP.
