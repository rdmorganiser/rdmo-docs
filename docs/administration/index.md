# Administration

The Django framework offers a rich administration (or short admin) interface, which allows you to directly manipulate most of the entries in the database directly. Obviously, only users with the correct permissions are allowed to use this interface. The user created during the installation process using `./manage.py createsuperuser` has this *superuser* status.

The admin interface is available under the link *Admin* in the navigation bar. It will only be needed on rare occasions, since most of the configurations of the questionaire and the other RDMO functions can be done using the more user-friendly Management interface described [in the following chapter of this documentation](../../management/index.html)`.

That being said, the admin interface is needed, especially after installation, to set the title and URL of the [site](../../administration/site.html), to configure [users and groups](../../administration/users.html)`, to configure the connection to [OAUTH providers](../../administration/allauth.html), and to create [tokens](../../administration/tokens.html) to be used with the API.

```eval_rst
.. toctree::
   :maxdepth: 2

   site
   users
   allauth
   api
```
