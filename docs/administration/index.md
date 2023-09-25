# Administration

The Django framework offers a rich administration (or short admin) interface, which allows you to directly manipulate most of the entries in the database directly. Obviously, only users with the correct permissions are allowed to use this interface. The user created during the installation process using `./manage.py createsuperuser` has this *superuser* status.

The admin interface is available under the link *Admin* in the navigation bar. It will only be needed on rare occasions, since most of the configurations of the questionnaire and the other RDMO functions can be done using the more user-friendly Management interface described [in the following chapter of this documentation](../management/index).

That being said, the admin interface is needed, especially after installation, to set the title and URL of the [site](site), to configure [users and groups](users), to configure the connection to [OAUTH providers](allauth), and to create tokens to be used with the [API](api).

```eval_rst
----

.. toctree::
   :maxdepth: 2

   site
   users
   allauth
   api
```
