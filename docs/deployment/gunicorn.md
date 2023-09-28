# Gunicorn

As mentioned several times, you should create a dedicated user for RDMO. All steps for the installation, which do not need root access, should be done using this user. Here we assume this user is called `rdmo` and it's home is `/srv/rdmo` and therefore your `rdmo-app` is located in `/srv/rdmo/rdmo-app`.

First install gunicorn inside your virtual environment:

```bash
pip install rdmo[gunicorn]
```

Then, test `gunicorn` using:
```bash
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
```

This should serve the application like `runserver`, but without the static assets, like CSS files and images. After the test kill the `gunicorn` process again.

## Systemd

Systemd will launch the Gunicorn process on startup and keep running. Create a new systemd service file in `/etc/systemd/system/rdmo.service` and enter (you will need root/sudo permissions for that):

```
[Unit]
Description=RDMO gunicorn daemon
After=network.target

[Service]
User=rdmo
Group=rdmo

WorkingDirectory=/srv/rdmo/rdmo-app

LogsDirectory=gunicorn rdmo
RuntimeDirectory=gunicorn

Environment=GUNICORN_BIN=/srv/rdmo/rdmo-app/env/bin/gunicorn
Environment=GUNICORN_WORKER=3
Environment=GUNICORN_TIMEOUT=30
Environment=GUNICORN_BIND=unix:/run/gunicorn/rdmo.sock
Environment=GUNICORN_PID_FILE=/run/gunicorn/rdmo.pid
Environment=GUNICORN_ACCESS_LOG_FILE=/var/log/gunicorn/access.log
Environment=GUNICORN_ERROR_LOG_FILE=/var/log/gunicorn/error.log

ExecStart=/bin/sh -c '${GUNICORN_BIN} \
  --workers ${GUNICORN_WORKER} \
  --timeout ${GUNICORN_TIMEOUT} \
  --bind ${GUNICORN_BIND} \
  --pid ${GUNICORN_PID_FILE} \
  --access-logfile ${GUNICORN_ACCESS_LOG_FILE} \
  --error-logfile ${GUNICORN_ERROR_LOG_FILE} \
  config.wsgi:application'

ExecReload=/bin/sh -c '/usr/bin/pkill -HUP -F ${GUNICORN_PID_FILE}'

ExecStop=/bin/sh -c '/usr/bin/pkill -TERM -F ${GUNICORN_PID_FILE}'

[Install]
WantedBy=multi-user.target
```

If RDMO runs under a subpath or your domain (or alias, e.g. <https://example.com/rdmo/>), when you have set a value for `BASE_URL` in your [settings](../configuration/general). The `SCRIPT_NAME` environment variable needs to be set in the `ExecStart` call, e.g. `--env SCRIPT_NAME=/rdmo`.

After the service file is created and every time it is changed, `systemd` needs to be reloaded:

```bash
systemctl daemon-reload
```

The RDMO service needs to be started and enabled like any other service:


```bash
sudo systemctl start rdmo
sudo systemctl enable rdmo
```

Gunicorn is web server which runs locally and a **reverse proxy** is needed to allow connections from the internet. This can be done with a web server, e.g. NGINX or Apache2.

## NGINX as reverse proxy

Nginx can be installed on Debian or Ubuntu using:

```bash
sudo apt install nginx  # on Debian/Ubuntu
```

Edit the Nginx configuration as follows (again with root/sudo permissions):

```nginx
# in /etc/nginx/sites-available/default  on Debian/Ubuntu
server {
    listen 80;
    server_name YOURDOMAIN;

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_pass http://unix:/run/gunicorn/rdmo/rdmo.sock;
    }

    location /static/ {
        alias /srv/rdmo/rdmo-app/static_root/;
    }
}
```

Restart and enable Nginx:

```bash
systemctl start nginx
systemctl enable nginx
```


 RDMO should now be available on `YOURDOMAIN`. Note that the unix socket `/srv/rdmo/rdmo.sock` needs to be accessible by Nginx.

## Apache2 as reverse proxy

Apache can be installed on Debian or Ubuntu using:

```bash
sudo apt install apache2
```


Edit the Apache configuration as follows (again with root/sudo permissions):

```apache
# in /etc/apache2/sites-available/default  on Debian/Ubuntu
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    <Location />

    </Location>

    Alias /static /srv/rdmo/rdmo-app/static_root/
    <Directory /srv/rdmo/rdmo-app/static_root/>
        Require all granted
    </Directory>
</VirtualHost>
```

Restart and enable Apache:

```bash
systemctl start apache2
systemctl enable apache2
```

## Static assets

As you can see from the virtual host configurations, the static assets such as CSS and JavaScript files are served independently from the reverse proxy to the gunicorn process. In order to do so they need to be gathered in the `static_root` directory. This can be achieved by running:

```bash
python manage.py collectstatic --clear
```

in your virtual environment (`--clear` removes existing files before collecting).

In order to apply changes to the RDMO code (e.g. after an [upgrade](../upgrade/index)), the Gunicorn process needs to be restarted:

```
sudo systemctl restart rdmo
```
