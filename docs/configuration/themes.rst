Themes
------

Introduction
````````````

RDMO is based on Django, which allows a high level of customization by modifying the Django *templates* as well as the *static assets* (CSS file, images, etc.). There is a powerful method by which the set of files getting imported can be changed. If you create a ``theme`` folder in your ``rdmo-app`` directory the framework will use the files in this folder and not their counterparts from the RDMO installation. By doing this you can override any template or static file you desire as long as you get the folder structure right. There are two ways to create a theme.

Create manually
```````````````

If you want to manually create a theme you need to do the following:

1. create a ``theme`` folder containing a ``static`` and a ``templates`` directory inside your ``rdmo-app`` directory

.. code:: python

    mkdir -p theme/static theme/templates

2. Add the line below to your ``config/settings/local.py``

.. code:: python

    THEME_DIR = os.path.join(BASE_DIR, 'theme')

3. Copy the files you want to modify into the `theme` folder keeping their relative paths. Please see below for further advice.

Create automatically
````````````````````

There is a ``manage.py`` script to simplify the theme creation. The script will create the ``theme/static`` and ``theme/templates`` folders, copy a basic set of files into them and add the necessary config line to the ``local.py`` to enable the theme. If you want to override other files, please put them into the necessary folders manually. To run the script do:

.. code:: shell

    python manage.py make_theme

Working with themes
-------------------

If you have completed these steps templates and static files in the ``theme`` directory are used instead of the original files as long as they have the same relative path, e.g. the template ``theme/templates/core/base_navigation.html`` overrides ``rdmo/core/templates/core/base_navigation.html`` from the original code.

Usually, the RDMO template files are located in the your virtual environment, e.g. ``/srv/rdmo/rdmo-app/env/lib/python2.7/site-packages/rdmo/core/static/core/css/variables.scss``. The exact path depends on your Python version and platform. We recomended to download the original files from the `rdmo repository <https://github.com/rdmorganiser/rdmo>`_ instead. For the example above, this would be https://raw.githubusercontent.com/rdmorganiser/rdmo/master/rdmo/core/static/core/css/variables.scss. Please make sure that you use the raw files if you download from github. If you accidentally grab the website html source RDMO will break.

Some files you might want to override are:

SASS variables
    https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/static/core/css/variables.scss can be copied to ``theme/static/core/css/variables.scss`` and be used to customize colors.

Navigation bar
    https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/templates/core/base_navigation.html can be copied to ``theme/templates/core/base_navigation.html`` and be used to customize the navbar.

Home page text
    https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/templates/core/home_text_en.html and https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/templates/core/home_text_de.html can be copied to ``theme/templates/core/home_text_en.html`` and ``theme/templates/core/home_text_de.html`` and be used to customize text on the home page.

Terms of Use
    The content displayed in the Terms of Use dialogue can be customized by putting templates to the appropriate locations. Two different files resembling the available languages can be used and should be located at ``theme/templates/account/terms_of_use_de.html`` and  ``theme/templates/account/terms_of_use_en.html``. Set the variable ACCOUNT_TERMS_OF_USE to True in your config/settings/local.py.


Note that updates to the RDMO package might render your theme incompatible to the RDMO code and cause errors. In this case the files in ``theme`` need to be adjusted to match their RDMO counterparts in functionality.
