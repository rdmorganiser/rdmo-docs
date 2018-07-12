Swagger / OpenAPI
=================

What is Swagger?
----------------
Swagger is a set of tools built around the OpenAPI Specification. These tools help to design, build and document REST APIs. OpenAPI is already implemented in RDMO but usually disabled. The Swagger page in RDMO is provided by a python library called `Django REST Swagger <https://github.com/marcgibbons/django-rest-swagger>`_ .


Enable Swagger Tools
--------------------
If you want to have a look at a detailed description of all the API interfaces that RDMO provides you need to add the necessary import and setup a url scheme to access the view.

All this can be achieved by adding two lines to the ``config/settings/urls.py`` in your RDMO-App. Please note that ``urlpatterns`` is an array. Do not simply copy the snippet from below but add the array entry into your already existing one.

.. code:: python

    from rdmo.core.swagger import swagger_schema_view

    urlpatterns = [
        url(r'^swagger$', swagger_schema_view.as_view()),
    ]


The Swagger page can now be accessed at the defined URL scheme. In the case of the example above at ``swagger/``. Of course you are free to change this to fit your needs.
