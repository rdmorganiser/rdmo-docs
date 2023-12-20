# Upgrade

The `rdmo` package can be conveniently upgraded using the `pip` command. However, before you perform any changes to your installation, please back up the important components to a save location.

A PostgreSQL or MySQL database can be database can be dumped into a file using:

```bash
pg_dump [DBNAME] > rdmo.sql  # PostgreSQL
mysqldump -uroot -p [DBNAME] > rdmo.sql
```

Your `rdmo-app` directory (including any sqlite3 database) can be copied using the usual commands. Note that your virtual environment will not work after being moved to a different path.

In order to upgrade your RDMO installation go to your `rdmo-app` directory, activate your virtual environment, and upgrade the `rdmo` package using `pip`:

```bash
pip install --upgrade rdmo
```

In order to install a specific version (e.g. 0.9.0) of RDMO use:

```bash
pip install --upgrade rdmo==0.9.0
```

After the upgrade a database migration might be necessary:

```bash
python manage.py migrate
```

Sometimes, the static vendor files need to be downloaded again:

```bash
python manage.py download_vendor_files
```

In any case you have to deploy the changes:

```
python manage.py deploy
```

The last three commands can be combined using:

```
python manage.py upgrade
```

Please check the release notes if this, or other, steps are necessary.

## Upgrade to version 2.0.0

**Important:** RDMO 2.0.0 uses Django 4.2 which drops support for older versions of Python (3.7), PostgreSQL (11), MySQL (5.7), and MariaDB (10.3), which are out of upstream support. Please check **before** updating if your machine is still able to run RDMO after the update. See also: https://docs.djangoproject.com/en/4.2/releases/4.2/#backwards-incompatible-changes-in-4-2.

```bash
python --version         # or python3 --version if you have still a python2 version
ls /usr/lib/postgresql/  # should show a directory with the version number
mysqld --version
``` 

If your system is too old, we suggest upgrading to the latest version of your distribution. If that is not possible, please look for means to update the software separately. If you run into trouble, please feel free to contact us.

With version 2.0.0 we have changed the data model and introduced pages, but this transition should automatically be applied to your content with the database migrations.

We have also reworked the rdmo package and updated some dependencies. Therefore, **when you use allauth for authentication**, you need to update this dependency separately from now on by using:

```bash
pip install rdmo[allauth]
```

You also need to add the following to your `config/settings/local.py`:

```python
from . import MIDDLEWARE  # if this import is not already present in the file
MIDDLEWARE.append('allauth.account.middleware.AccountMiddleware')
```

RDMO 2.0.0 uses Django 4.2, which removed some functions. If you use

```python
from django.utils.translation import ugettext_lazy as _
```

in your `config/settings/local.py`, you need to change this to

```python
from django.utils.translation import gettext_lazy as _
```

We have also refactored the `rdmo-app`, which people clone to start using RDMO. You should still be able to use your old `rdmo-app`, but you might take a look at [github.com/rdmorganiser/rdmo-app](https://github.com/rdmorganiser/rdmo-app) and adopt some of the new layout to your installation.

Instead of 6 seperate pages, RDMO now uses only one management interface at `/management/`. If you adjusted `core/base_navigation.html` in your theme, you need to change the link and the corresponding permission check. Instead of:

```django
{% has_perm 'questions.view_catalog' request.user as can_view_catalog %}
{% has_perm 'domain.view_attribute' request.user as can_view_attribute %}
{% has_perm 'options.view_optionset' request.user as can_view_optionset %}
{% has_perm 'conditions.view_condition' request.user as can_view_condition %}
{% has_perm 'tasks.view_task' request.user as can_view_task %}
{% has_perm 'views.view_view' request.user as can_view_view %}

{% if can_view_catalog or can_view_attribute or can_view_optionset or can_view_condition or can_view_task or can_view_view %}
<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
        {% trans 'Management' %}<span class="caret"></span>
    </a>
    <ul class="dropdown-menu">
        ...
    </ul>
</li>
{% endif %}
```

you need to use:

```django
{% test_rule 'management.can_view_management' request.user request.site as can_view_management %}

{% if can_view_management %}
<li>
    <a href="{% url 'management' %}">{% trans 'Management' %}</a>
</li>
{% endif %}
```

(Source file: https://github.com/rdmorganiser/rdmo/blob/2.0.0/rdmo/core/templates/core/base_navigation.html#L22.)

We also needed to adjust the `core/base.html` template. In the case that you use your own `core/base.html`, make sure that the `<head>` contains the following:

```django
{% load static compress core_tags %}<!DOCTYPE html>
<html>
<head>
    {% include 'core/base_head.html' %}

    {% block vendor %}
    {% vendor 'jquery' %}
    {% vendor 'bootstrap' %}
    {% vendor 'font-awesome' %}
    {% endblock %}

    {% block css %}
    {% compress css %}
    <link rel="stylesheet" type="text/x-scss" href="{% static 'core/css/base.scss' %}" />
    <link rel="stylesheet" type="text/x-scss" href="{% static 'core/css/fonts.scss' %}" />
    <link rel="stylesheet" type="text/x-scss" href="{% static 'core/css/footer.scss' %}" />
    <link rel="stylesheet" type="text/x-scss" href="{% static 'core/css/utils.scss' %}" />
    <link rel="stylesheet" type="text/x-scss" href="{% static 'core/css/style.scss' %}" />
    {% endcompress %}
    {% endblock %}

    {% block js %}
    {% endblock %}

    {% block head %}{% endblock %}
</head>
```

(Source file: https://github.com/rdmorganiser/rdmo/blob/2.0.0/rdmo/core/templates/core/base.html.)

## Upgrade to version 0.9.0

With version 0.9.0 we introduced the split into the `rdmo-app` and the centrally maintained `rdmo` package. Therefore, a few additional steps are needed to upgrade any earlier version to 0.9.0 or beyond:

1.  In any case perform a backup of your `rdmo` directory and your database as described above.

1.  Perform the steps described in [clone](../installation/clone) and [packages](../installation/packages) as if you would install a new instance of RDMO.

1.  Copy your old configuration from `/path/to/old/rdmo/rdmo/settings/local.py` to `/path/to/new/rdmo-app/config/settings/local.py`. The new `config` directory replaces the old `rdmo` directory.

1.  If you already have a `theme` directory, copy it into the new `rdmo-app` folder.

1.  Run a database migration (Unless you skipped several versions, the output should be `No migrations to apply.`):

    ```bash
    python manage.py migrate
    ```

1.  Download the front-end files from the CDN. We don't use bower and npm anymore.

    ```bash
    python manage.py download_vendor_files
    ```

1.  Update the path to the `wsgi.py` script in your Apache or nginx configuration. It is now under `/path/to/new/rdmo-app/config/wsgi.py`.

1.  Redeploy RDMO as described under deployment of [Apache](../deployment/apache) or [Gunicorn and Nginx](../deployment/gunicorn).

If you have trouble with the upgrade process, don't hesitate to contact the RDMO team for support.

## Upgrade to version 0.14

With version 0.14 the Python 2 support was dropped and we switched to Django 2.2. This demands two changes to the local `rdmo-app`:

* Adjust RDMO app's `config/urls.py` to Django2 schemes. The file is much simpler and shorter now. A working example can be found at https://github.com/rdmorganiser/rdmo-app/blob/master/config/urls.py
* MIDDLEWARE_CLASSES in `config/settings/local.py` needs to be renamed to `MIDDLEWARE` only

---

```{warning}
RDMO contains all the necessary migrations. For consistency of the database,
please do **not** run the ``makemigrations`` command. When Django asks you for it, please contact support.
```