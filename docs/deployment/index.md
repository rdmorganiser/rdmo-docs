# Deployment

As already mentioned, RDMO can be run in two different setups:

1. For development or testing, using the built-in Django development server<br>
Information about how to do that can be found in the [development section](../development/index).
<br><br>
1. In production, using a web server and the [wsgi](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/) protocol<br>
We suggest to use one of the following setups:
    * [Apache2 and mod_wsgi](apache) (Shibboleth can only be used with this setup.)
    * [Gunicorn](gunicorn)

---

```{toctree}
:maxdepth: 2

development
apache
gunicorn
```
