# LDAP

## Prerequisites

In order to use a LDAP backend with RDMO you need to install some prerequistes. On Debian/Ubuntu you can install them using:

```bash
sudo apt-get install libsasl2-dev libldap2-dev libssl-dev
```

On the python side, we use [django-auth-ldap](https://pypi.org/project/django-auth-ldap) to connect to the LDAP server. As before, it should be installed inside the virtual environment created for RDMO using:

```bash
pip install rdmo[ldap]
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

## Configuration

In order to use LDAP as one of your authentication backends in RDMO, edit `config/settings/local.py` and add or uncomment:

```python
import ldap
from django_auth_ldap.config import LDAPSearch

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

The setting `PROFILE_UPDATE = False` and `PROFILE_DELETE = False` tell RDMO to disable the update and deletion form for the user profile so that users can neither update their credentials nor delete their profile anymore.

The other settings are needed by `django-auth-ldap` and are described in the [django-auth-ldap documentation](https://django-auth-ldap.readthedocs.io/en/latest/).

For an LDAP connection to an Active Directory, the configuration differs slightly:

```python
import ldap
from django_auth_ldap.config import LDAPSearch

PROFILE_UPDATE = False
PROFILE_DELETE = False

AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
AUTH_LDAP_BIND_DN = "cn=RDMO_LDAP_ACCOUNT_CN,dc=ldap,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "RDMO_LDAP_ACCOUNT_PASSWORD"
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=ldap,dc=example,dc=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
AUTH_LDAP_CONNECTION_OPTIONS = {ldap.OPT_REFERRALS: 0}

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

Again, your particular setup might differ.

## Groups

You can also map LDAP groups to Django groups, in particular to restrict the access to Catalogs and Views. This can be done by adding the following settings:

```python
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "dc=ldap,dc=test,dc=rdmo,dc=org", ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
AUTH_LDAP_MIRROR_GROUPS = ['special']
```

where `cn` is the name of the particular group in the LDAP and `AUTH_LDAP_MIRROR_GROUPS` denotes the groups which are actually mirrored from the LDAP.

## Signals 

[django-auth-ldap](https://pypi.org/project/django-auth-ldap) offers a [Django signal](https://docs.djangoproject.com/en/4.2/topics/signals/) to perform follow up actions after the creation of the user model (but before saving it). See: <https://django-auth-ldap.readthedocs.io/en/latest/reference.html#django_auth_ldap.backend.populate_user>.

We can use this to put every LDAP user in the `ldap` group (but not users from other authentication methods). Just put the following code in the `models.py` (which is read by the server automatcally) of the [local theme app](../../themes/index.md#themes) in your `rdmo-app`:

```python
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_auth_ldap.backend import populate_user


@receiver(populate_user)
def handle_populate_ldap_user(sender, user, ldap_user, **kwargs):
    user.is_ldap = True


@receiver(post_save, sender=User)
def handle_post_save_ldap_user(sender, instance, **kwargs):
    if getattr(instance, 'is_ldap', None):
        group, created = Group.objects.get_or_create(name='ldap')
        instance.groups.add(group)
```
