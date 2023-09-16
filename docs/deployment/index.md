# Deployment

As already mentioned, RDMO can be run in two different setups:

1. For development or testing, using the built-in Django development server<br>
Information about how to do that can be found in the [docs of the RDMO repository](https://github.com/rdmorganiser/rdmo/tree/master/docs).
<br><br>
1. In production, using a web server and the [wsgi](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/) protocol<br>
We suggest to use one of the following setups:
    * [Apache2 and mod_wsgi](apache.html) (Shibboleth can only be used with this version.)
    * [nginx, gunicorn and systemd](nginx.html)


```eval_rst
----

.. toctree::
   :maxdepth: 2

   development
   apache
   nginx
```
