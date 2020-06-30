Multisite
=========

```eval_rst
.. warning::
    This is an advanced feature of RDMO.
```

RDMO can be operated in a multi site setup, connecting several different `rdmo-apps` with different URLs and Themes, on one Server with one common Database. The different Sites will share their Catalogs, Views, etc., but the availability of this Content can be restricted among the Sites. Users can log in into any of the sites (if the authentication method allows) and projects can be shared among sites. Each of these RDMO Sites has its own `rdmo-app` directory and its own configuration (`config/settings/local.py`).

Setup
-----

To setup such a multi site installation, you need to start with a regular RDMO instance as described in [installation](../installation/index.html). In principle, an existing RDMO instance can be extended to a multi site installation, but in this documentation we assume a fresh installation.

* Create the virtual enviroment outside the `rdmo-app`, e.g. in `/srv/rdmo/env`. In a multi site setup all RDMO sites use **the same** virtual enviroment. RDMO and the other python dependencies need to be updated only once for the whole installation.

* Otherwise, follow the instructions as usual, but add `MULTISITE = True` to `config/settings/local.py`. This enables the multi site features in the user interface.

* After the installation, login to the admin interface and add your additional sites in the Sites section as described [here](../administration/site.html). Note the numerical ID of the different Sites as shown in the URL when editing the Site (e.g. `http://localhost:8000/admin/sites/site/2/change/`).

* Then clone a second `rdmo-app` next to the first one, but use the same virtual environement as before (so no `pip install` is required). Setup `rdmo-app2/config/settings/local.py` as usual. Include `MULTISITE = True` and `SITE_ID = X` in `rdmo-app2/config/settings/local.py`, where `X` is the ID of the site from the step before. For `DATABASE` use the **same** settings as in `rdmo-app`.

If you now run `./manage.py runserver 0.0.0.0:8000` in `rdmo-app` and `./manage.py runserver 0.0.0.0:8002` in `rdmo-app2`, the two sites should be working already.

Deployment
----------

The two sites are deployed seperately, regardles if using Apache or nginx. Create seperate virtual host configurations which map the particular site url to the corresponding `rdmo-app`. E.g. for Apache:

```
<VirtualHost *:443>
    ServerName example.com

    ...

    Alias /static /srv/rdmo/rdmo-app/static_root/
    <Directory /srv/rdmo/rdmo-app/static_root/>
        Require all granted
    </Directory>

    WSGIDaemonProcess rdmo_app user=rdmo group=rdmo \
        home=/srv/rdmo/rdmo-app python-home=/srv/rdmo/env
    WSGIProcessGroup rdmo_app
    WSGIScriptAlias / /srv/rdmo/rdmo-app/config/wsgi.py process-group=rdmo_app
    WSGIPassAuthorization On

    <Directory /srv/rdmo/rdmo-app/config/>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
</VirtualHost>
```

and

```
<VirtualHost *:443>
    ServerName example.org

    ...

    Alias /static /srv/rdmo/rdmo-app2/static_root/
    <Directory /srv/rdmo/rdmo-app2/static_root/>
        Require all granted
    </Directory>

    WSGIDaemonProcess rdmo_app2 user=rdmo group=rdmo \
        home=/srv/rdmo/rdmo-app2 python-home=/srv/rdmo/env
    WSGIProcessGroup rdmo_app2
    WSGIScriptAlias / /srv/rdmo/rdmo-app2/config/wsgi.py process-group=rdmo_app2
    WSGIPassAuthorization On

    <Directory /srv/rdmo/rdmo-app2/config/>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
</VirtualHost>
```

Shibboleth
----------

In order to run multiple seperate sites on one machine the Service Provider needs to be configured differently. For each site but the first one, an `ApplicationOverride` needs to be configured in `/etc/shibboleth/shibboleth2.xml`, e.g.

```xml
<SPConfig xmlns="urn:mace:shibboleth:3.0:native:sp:config"
    xmlns:conf="urn:mace:shibboleth:3.0:native:sp:config"
    clockSkew="180">

    <OutOfProcess tranLogFormat="%u|%s|%IDP|%i|%ac|%t|%attr|%n|%b|%E|%S|%SS|%L|%UA|%a" />

    <ApplicationDefaults entityID="https://sp.test.rdmo.org/shibboleth"
        REMOTE_USER="eppn"
        cipherSuites="DEFAULT:!EXP:!LOW:!aNULL:!eNULL:!DES:!IDEA:!SEED:!RC4:!3DES:!kRSA:!SSLv2:!SSLv3:!TLSv1:!TLSv1.1">

        <Sessions lifetime="28800" timeout="3600" relayState="ss:mem"
                  checkAddress="false" handlerSSL="true" cookieProps="https">
            <SSO entityID="https://idp.test.rdmo.org/idp/shibboleth"
                 discoveryProtocol="SAMLDS" discoveryURL="https://ds.example.org/DS/WAYF">SAML2</SSO>

            ...

        </Sessions>

        ...

        <AttributeFilter type="XML" validate="true" path="attribute-policy.xml"/>
            <CredentialResolver type="File" use="signing" key="sp-key.pem" certificate="sp-cert.pem"/>
            <CredentialResolver type="File" use="encryption" key="sp-key.pem" certificate="sp-cert.pem"/>

        <MetadataProvider type="XML" validate="true" path="idp-metadata.xml"/>

        <ApplicationOverride id="sp2" entityID="https://sp2.test.rdmo.org/shibboleth">
            <Sessions lifetime="28800" timeout="3600" relayState="ss:mem"
                      checkAddress="false" handlerSSL="true" cookieProps="https">
                <SSO entityID="https://idp2.test.rdmo.org/idp/shibboleth"
                     discoveryProtocol="SAMLDS" discoveryURL="https://ds.example.org/DS/WAYF">SAML2</SSO>

                ...

            </Sessions>

            <CredentialResolver type="File" use="signing" key="sp2-key.pem" certificate="sp2-cert.pem"/>
            <CredentialResolver type="File" use="encryption" key="sp2-key.pem" certificate="sp2-cert.pem"/>
            <MetadataProvider type="XML" validate="true" path="idp2-metadata.xml"/>
        </ApplicationOverride>

    </ApplicationDefaults>

    ...

</SPConfig>
```

where `https://idp.test.rdmo.org` und `https://idp2.test.rdmo.org/idp/shibboleth` are two different IdP for the two RDMO sites. Again, your Shibboleth setup might differ.

In the virtual host configuration for each but the first site, `ShibRequestSetting applicationId <id>` needs to be added to both `<Location /Shibboleth.sso>` and `<LocationMatch /(...)>`. `<id>` is the `id` attribute of the `ApplicationOverride` node, e.g.:

```
<Location /Shibboleth.sso>
    SetHandler shib
    ShibRequestSetting applicationId example.org
</Location>
<LocationMatch /(account|domain|options|projects|questions|tasks|conditions|views)>
    AuthType shibboleth
    require shibboleth
    ShibRequireSession On
    ShibUseHeaders On
    ShibRequestSetting applicationId example.org
</LocationMatch>
```

