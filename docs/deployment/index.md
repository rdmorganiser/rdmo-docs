# Deployment

As already mentioned, RDMO can be run in two different setups:

* for [development or testing](development), using the build-in Django development server.

* in production, using a web server and the [wsgi](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/) protocoll. We suggest to use one of the following setups:

    * :doc:`Apache2 and mod_wsgi <apache>` (Shibboleth can only be used with this version.)
    * :doc:`nginx, gunicorn and systemd <nginx>`


```eval_rst
.. toctree::
   :maxdepth: 2

   development
   apache
   nginx
```
