Multisite
=========

```eval_rst
.. warning::
    The following feature is not available in the released version of RDMO yet. It will be part of a future version.
```

RDMO can be operated in a multi site setup, connecting several different `rdmo-apps` with different URLs and Themes, on one Server with one common Database. The different Sites will share their Catalogs, Views, etc., but the availability of this Content can be restricted among the Sites. Projects will have a connection to a particular site and can only be accessed on the webpage which they were created on.

Setup
-----

To setup such a multi site installation, you need to start with a regular RDMO instance as described in [installation](../installation).

* Create the virtual enviroment outside the `rdmo-app`, e.g. in `/srv/rdmo/env`. Otherwise, follow the instructions as usual, but add `MULTISITE = True` to `config/settings/local.py`. This enables the multi site features in the user interface.

* After the installation, login to the admin interface and add your additional sites in the Sites section as described [here](../administration/site). Note the numerical ID of the different Sites as shown in the URL when editing the Site (e.g. `http://localhost:8000/admin/sites/site/2/change/`).

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
<ApplicationOverride id="example.org" entityID="https://example.org/shibboleth">
    <CredentialResolver type="File" use="signing" key="example-org-key.pem" certificate="example-org-cert.pem"/>
    <CredentialResolver type="File" use="encryption" key="example-org-key.pem" certificate="example-org-cert.pem"/>
</ApplicationOverride>
```

where `example-org-key.pem` and `example-org-cert.pem` are the private key and public certificate for this URL. Again, your Shibboleth setup might differ.

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

