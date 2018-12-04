# Deployment

As already mentioned, RDMO can be run in two different setups:

* for [development or testing](../../deployment/development.html), using the build-in Django development server.

* in production, using a web server and the [wsgi](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/) protocol. We suggest to use one of the following setups:

    * [Apache2 and mod_wsgi](../../deployment/apache.html) (Shibboleth can only be used with this version.)
    * [nginx, gunicorn and systemd](../../deployment/nginx.html)


```eval_rst
.. toctree::
   :maxdepth: 2

   development
   apache
   nginx
```
