# Nginx and Gunicorn

As mentioned several times, you should create a dedicated user for RDMO. All steps for the installation, which do not need root access, should be done using this user. Here we assume this user is called `rdmo` and it's home is `/srv/rdmo` and therefore your `rdmo-app` is located in `/srv/rdmo/rdmo-app`.

First install gunicorn inside your virtual environment:

```bash
pip install -r requirements/gunicorn.txt
```

Then, test `gunicorn` using:
```bash
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
```

This should serve the application like `runserver`, but without the static assets, like CSS files and images. After the test kill the `gunicorn` process again.

Systemd will launch the Gunicorn process on startup and keep running. Create a new systemd service file in `/etc/systemd/system/rdmo.service` and enter (you will need root/sudo permissions for that):

```
[Unit]
Description=RDMO gunicorn daemon
After=network.target

[Service]
User=rdmo
Group=rdmo
WorkingDirectory=/srv/rdmo/rdmo-app
ExecStart=/srv/rdmo/rdmo-app/env/bin/gunicorn \
    --bind unix:/srv/rdmo/rdmo.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
```

This service needs to be started and enabled like any other service:

```bash
sudo systemctl start rdmo
sudo systemctl enable rdmo
```

Next, install Nginx:

```bash
sudo apt install nginx  # on Debian/Ubuntu
sudo yum install nginx  # on RHEL/CentOS
```

Edit the Nginx configuration as follows (again with root/sudo permissions):

```nginx
# in /etc/nginx/sites-available/default  on Debian/Ubuntu
# in /etc/nginx/conf.d/vhost.conf        on RHEL/CentOS
server {
    listen 80;
    server_name YOURDOMAIN;

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_pass http://unix:/srv/rdmo/rdmo.sock;
    }

    location /static/ {
        alias /srv/rdmo/rdmo-app/static_root/;
    }
}
```

Restart Nginx. RDMO should now be available on `YOURDOMAIN`. Note that the unix socket `/srv/rdmo/rdmo.sock` needs to be accessible by Nginx.

As you can see from the virtual host configurations, the static assets such as CSS and JavaScript files are served independently from the reverse proxy to the gunicorn process. In order to do so they need to be gathered in the `static_root` directory. This can be achieved by running:

```bash
python manage.py collectstatic --clear
```

in your virtual environment (`--clear` removes existing files before collecting).

In order to apply changes to the RDMO code (e.g. after an [upgrade](../upgrade/index.html)), the Gunicorn process needs to be restarted:

```
sudo systemctl restart rdmo
```
