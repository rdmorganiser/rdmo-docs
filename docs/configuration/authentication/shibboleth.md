# Shibboleth

In order to use Shibboleth with RDMO, it needs to be deployed in a production environment using Apache2. The Setup is documented [here](/deployment/apache.html).

Next, install the Shibboleth Apache module for the service provider (SP) from your distribution repository, e.g. for Debian/Ubuntu:

```bash
sudo apt-get install libapache2-mod-shib2
```

Under Ubuntu 18.04 LTS the `libapache2-mod-shib2` package is broken. A working description on how to install the SPcan be found under https://www.switch.ch/aai/guides/sp/installation/?os=ubuntu.

In addition, [django-shibboleth-remoteuser](https://github.com/Brown-University-Library/django-shibboleth-remoteuser) needs to be installed in your RDMO virtual environment:

```bash
pip install -r requirements/shibboleth.txt
```

Configure your Shibboleth service provider using the files in `/etc/shibboleth/`. This may vary depending on your Identity Provider. RDMO needs the `REMOTE_SERVER` to be set and 4 attributes from your identity provider:

* a username (usually `eppn`)
* an E-mail address (usually `mail` or `email`)
* a first name (usually `givenName`)
* a last name (usually `sn`)

In our test environent this is accomplished by editing `/etc/shibboleth/shibboleth2.xml`:

```xml
<ApplicationDefaults entityID="https://sp.test.rdmo.org/shibboleth"
    REMOTE_USER="eppn"
    cipherSuites="DEFAULT:!EXP:!LOW:!aNULL:!eNULL:!DES:!IDEA:!SEED:!RC4:!3DES:!kRSA:!SSLv2:!SSLv3:!TLSv1:!TLSv1.1">
```

and `/etc/shibboleth/attribute-map.xml`:

```xml
<Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.6" id="eppn">
    <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
</Attribute>
<Attribute name="urn:oid:0.9.2342.19200300.100.1.1" id="uid"/>
<Attribute name="urn:oid:2.5.4.4" id="sn"/>
<Attribute name="urn:oid:2.5.4.42" id="givenName"/>
<Attribute name="urn:oid:0.9.2342.19200300.100.1.3" id="mail"/>
```

Restart the Shibboleth service provider demon.

```bash
service shibd restart
```

In your Apache2 virtual host configuration, add:

```
<Location /Shibboleth.sso>
    SetHandler shib
</Location>
<LocationMatch /(account|domain|options|projects|questions|tasks|conditions|views)>
    AuthType shibboleth
    require shibboleth
    ShibRequireSession On
    ShibUseHeaders On
</LocationMatch>
```

In your `config/settings/local.py` add or uncomment:

```python
from rdmo.core.settings import INSTALLED_APPS, AUTHENTICATION_BACKENDS, MIDDLEWARE_CLASSES

SHIBBOLETH = True
PROFILE_UPDATE = False
PROFILE_DELETE = False

INSTALLED_APPS += ['shibboleth']

AUTHENTICATION_BACKENDS.append('shibboleth.backends.ShibbolethRemoteUserBackend')
MIDDLEWARE_CLASSES.insert(
    MIDDLEWARE_CLASSES.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
    'shibboleth.middleware.ShibbolethRemoteUserMiddleware'
)

SHIBBOLETH_ATTRIBUTE_MAP = {
    'uid': (True, 'username'),
    'givenName': (True, 'first_name'),
    'sn': (True, 'last_name'),
    'mail': (True, 'email'),
}

LOGIN_URL = '/Shibboleth.sso/Login?target=/projects'
LOGOUT_URL = '/Shibboleth.sso/Logout'
```

where the keys of `SHIBBOLETH_ATTRIBUTE_MAP`, `LOGIN_URL`, and `LOGOUT_URL` need to be modified according to your setup. The setting `SHIBBOLETH = True` disables the regular login form in RDMO, and tells RDMO to disable the update or delete form for the user profile, so that users can neither update their credentials nor delete their profile anymore. Note that profile deletion is technically impossible because RDMO can delete from the Shibboleth database. The `INSTALLED_APPS`, `AUTHENTICATION_BACKENDS`, and `MIDDLEWARE_CLASSES` settings enable django-shibboleth-remoteuser to be used with RDMO.

Restart the webserver.

```bash
service apache2 restart
```

```eval_rst
.. warning::
    The following feature is not available in the released version of RDMO yet. It will be part of a future version.
```

Certain Attributes from the Shibboleth Identity Provider can be mapped to Django groups, in particular to restrict the access to Catalogs and Views. This can be done by adding the following settings:

```
SHIBBOLETH_GROUP_ATTRIBUTES = ['eduPersonScopedAffiliation']
```

In this case, the attribute `eduPersonScopedAffiliation` contains a comma seperated list of groups which will be created in RDMO (if they don't exist yet) and the user will be added into these groups. Due to a limitation by [django-shibboleth-remoteuser](https://github.com/Brown-University-Library/django-shibboleth-remoteuser) the user will also be **removed from all other groups**.
