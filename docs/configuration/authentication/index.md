# Authentication

RDMO has three main modes for Authentication:

* Regular user accounts with registration using the [django-allauth](allauth) library.
* Using a (read-only) connection to a [LDAP server](ldap)
* Installing a [Shibboleth](shibboleth) service provider next to RDMO and connect to an identity provider or even a whole Shibboleth federation.

If none of the modes is enabled, only a very basic login will be available and users need to be created using the Django Admin Interface.

```eval_rst
----

.. toctree::

   allauth
   ldap
   shibboleth
```
