# Cache

```eval_rst
.. warning::
    As of RDMO 1.6, caching is not used anymore and memcached does not need to be installed anymore. However, if needed, we will enable this feature again in the future.
```

RDMO uses a cache for some of it's pages. In the development setup, this is done using local-memory caching. In production, we suggest using [memcached](https://memcached.org) Memcached can be installed on Debian/Ubuntu using:

```bash
sudo apt install memcached
```

On RHEL/CentOS a few more steps are needed. First install the package using:

```
sudo yum install memcached
```

Then edit the settings file to prevent external connections:

```bash
# in /etc/sysconfig/memcached
PORT="11211"
USER="memcached"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS="-l 127.0.0.1"
```

Then start the service:

```bash
systemctl start memcached
systemctl enable memcached
```

Back in your virtual environment, according to [docs.djangoproject.com/en/4.2/topics/cache](https://docs.djangoproject.com/en/4.2/topics/cache/#memcached), you need to install `pymemcache`:

```bash
pip install pymemcache
```

and add the following to your `config/settings/local.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'rdmo_default'
    },
    'api': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'rdmo_api'
    }
}
```
