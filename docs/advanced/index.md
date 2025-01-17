# Advanced topics

## SELinux

For distributions that use SELinux (e.g. CentOS, RHEL, Fedora), the following commands can be used to configure SELinux:

```bash
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/rdmo/rdmo-app(/.*)?"
sudo semanage fcontext -a -t httpd_sys_rw_content_t "/srv/rdmo/rdmo-app/static_root/CACHE(/.*)?"
sudo semanage fcontext -a -t httpd_sys_rw_content_t "/srv/rdmo/rdmo-app/log(/.*)?"
sudo semanage fcontext -a -t httpd_sys_script_exec_t -f f "/srv/rdmo/rdmo-app/env(/.*)?/.+\.so(\.[^/]*)*"
sudo restorecon -R -v /srv/rdmo
sudo setsebool -P httpd_can_network_connect=1
```

While this is the prefereble way, you can also set `selinux` to `permissive` or `disabled` in `/etc/selinux/config` (and reboot afterwards).

## Multiple Reverse Proxies

For special setups including multiple reverse proxies the configuration needs to be adjusted in order to successfully work.
The reason is that [django's CSRF protection](https://docs.djangoproject.com/en/4.2/ref/csrf/#how-it-works) requires a proper request header in order to not reject the request.
To achieve this, the first reverse proxy needs to set the corresponding X-Forwarded-* header, e.g. for nginx:

```
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $http_host;
```

All remaining proxies should not change these information, i.e. don't add such configuration.

**Additionally**, RDMO has to be adjusted according to the description for [reverse proxies](../configuration/general.html#optional-reverse-proxy).

## Install RDMO without internet connection

In order to install RDMO on a server without (outgoing) internet connection, you need to download the Python packages on a different machine and copy the wheels to the server:

```bash
# on the machine with internet
mkdir packages
cd packages
pip download pip setuptools wheel
pip rdmo[allauth,postgres,gunicorn] # or any other combination of optional dependencies
```

The `packages` should then contain `*.whl` files for all dependencies.

You also need to download the vendor files as in the regular setup:

```python
python manage.py download_vendor_files
```

Next you need to copy the `packages` and the `vendor` directory to the machine without internet. There, you copy the `vendor` directory to the `rdmo-app` directory, create a virtual env and install the pip dependencies using:

```bash
pip install --upgrade --no-index --find-links /path/to/packages/ pip setuptools wheel
pip install --upgrade --no-index --find-links /path/to/packages/ rdmo[allauth,postgres,gunicorn]
```

## Use uv to install a custom Python version

If you want to use a different Python version than your Linux distribution provides, you can use [uv](https://github.com/astral-sh/uv) to set it up. Note that this will only work for the Gunicorn setup. First install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then you can create a virtual environment with the desired Python version using, e.g.:

```bash
uv venv env --seed --python 3.12
```

## Content Security Policies

[Content Security Policies](https://en.wikipedia.org/wiki/Content_Security_Policy) are a security feature to tell the users browser to restrict what the web application is allowed to do. This is done by setting HTTP headers independent of the RDMO application.

For NGINX, you can create the following file in `/etc/nginx/snippets/security.conf`:

```nginx
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-eval' 'unsafe-inline'; style-src 'self' 'unsafe-inline';";
add_header Strict-Transport-Security "max-age=15768000";
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "no-referrer-when-downgrade";
add_header Permissions-Policy "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()";
```

The snippet is then included in the virtual host configuration using:

```
server {

    ...

    include /etc/nginx/snippets/security.conf;

    ...

}
```

The website <https://securityheaders.com/> can be used to check the headers.
