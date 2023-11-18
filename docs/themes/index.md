# Themes

## Introduction

RDMO is based on Django, which allows a high level of customization by modifying the Django *templates* as well as the *static assets* (CSS files, images, etc.). There is a powerful method by which the set of files getting imported can be changed. If you create a `rdmo_theme` app in your `rdmo-app` directory the framework will use the files in this folder and not their counterparts from the RDMO source code. By doing this you can override any template or static file you desire as long as you get the folder structure right. There are two ways to create a theme. We use `rdmo_theme` as name here, but you can use a different one.

In older versions of RDMO, did not use a Django app to create a theme, but simple directories `theme/static` and `theme/templates` and some additional configuration in `config/settings/__init__.py`. While this approach will continue to work and can be kept for existing instance, we encourage the use of Django apps for new themes.

## Create automatically

There is a `manage.py` script to simplify the theme creation. The script will create the `rdmo_theme/static` and `rdmo_theme/templates` folders as well as the `rdmo_theme/__init__.py` file which makes it a Python module. It also copies a basic set of files into them and adds the necessary configuration line to `config/settings/local.py` to enable the theme. To run the script do:

```bash
python manage.py make_theme
python manage.py make_theme --name=rdmo_cool  # for a cool theme name
```

If you want to override other files, you can use, e.g.:

```bash
python manage.py make_theme --file accounts/templates/account/terms_of_use_en.html
python manage.py make_theme --file accounts/templates/account/terms_of_use_de.html

# use the same --name as before
python manage.py make_theme --name=rdmo_cool --file=...
```

## Create manually

If you want to manually create a theme you need to do the following:

1. Create a `rdmo_theme` folder containing a `static` and a `templates` directory inside your `rdmo-app` directory:

    ```shell
    mkdir -p rdmo_theme/static rdmo_theme/templates
    touch rdmo_theme/__init__.py
    ```

2. Add the line below to your `config/settings/local.py`:

    ```python
    import os
    from . import INSTALLED_APPS

    INSTALLED_APPS = ['rdmo_theme'] + INSTALLED_APPS
    ```

3. Copy the files you want to modify into the `rdmo_theme` folder keeping their relative paths.


## Working with themes

If you have completed the steps above templates and static files in the `rdmo_theme` directory are used instead of the original files as long as they have the same relative path, e.g. the template `theme/templates/core/base_navigation.html` overrides `rdmo/core/templates/core/base_navigation.html` from the original code.

Usually, the RDMO template files are located in your virtual environment, e.g. `/srv/rdmo/rdmo-app/env/lib/python3.6/site-packages/rdmo/core/static/core/css/variables.scss`. The exact path depends on your Python version and platform. The `make_theme` script will find the files for you. You can also download the original files from the [rdmo repository](https://github.com/rdmorganiser/rdmo) instead. For the example above, this would be <https://raw.githubusercontent.com/rdmorganiser/rdmo/master/rdmo/core/static/core/css/variables.scss>. Please make sure to use the raw files when downloading from GitHub. If you accidentally grab the website's html source code RDMO will throw an error.

Some files you might want to override are:

### SASS variables

<https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/static/core/css/variables.scss> can be copied to `rdmo_theme/static/core/css/variables.scss` and be used to customize colors.

### Navigation bar

<https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/templates/core/base_navigation.html> can be copied to `rdmo_theme/templates/core/base_navigation.html` and be used to customize the navbar.

### Home page text

<https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/templates/core/home_text_en.html> and <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/templates/core/home_text_de.html> can be copied to `rdmo_theme/templates/core/home_text_en.html` and `rdmo_theme/templates/core/home_text_de.html` and be used to customize text on the home page.

### Terms of Use

The content displayed in the Terms of Use dialogue can be customized by putting templates to the appropriate locations. Two different files resembling the available languages can be used and should be located at `rdmo_theme/templates/account/terms_of_use_de.html` and  `rdmo_theme/templates/account/terms_of_use_en.html`. Set the variable `ACCOUNT_TERMS_OF_USE` to `True` in your `config/settings/local.py`.

Note that updates to the RDMO package might render your theme incompatible to the RDMO code and cause errors. In this case the files in `theme` need to be adjusted to match their RDMO counterparts in functionality.

### Emails

The emails, which are send to the users can be customized as well. Of particular interest is the template for mails inviting users to projects located at <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/templates/projects/email>. The templates can be copied to `rdmo_theme/templates/projects/email/project_invite_subject.txt` and `rdmo_theme/templates/projects/email/project_invite_message.txt` and edited accordingly.

## Custom translations

As described in the Introduction above RDMO themes are now supposed to be Django apps. Using this kind of themes brings another advantage regarding translations. It is possible to create custom .po files holding translations that then can be used along with the translations inside the RDMO core. Here are the steps to make this happen.

1. Create a theme if you do not have one already
    ```shell
    python manage.py make_theme
    ```

1. Ensure that the theme has a `locale` directory on it's top level (the folder added to `INSTALLED_APPS`).

1. Create the .po files for your translations. Note that the command has to be run inside the theme's folder.

    ```shell
    cd rdmo_theme
    django-admin makemessages -l de
    ```

1. Use [po edit](https://poedit.net/) or another tool of your choice to edit the po files inside the locale folder.

1. Compile the .mo files, if the tool does not do that on it's own.

    ```shell
    cd rdmo_theme
    django-admin compilemessages -l de
    ```

1. Make sure you have a folder structure equivalent to the one below. Especially regarding the location of the .po files.

    ```
    rdmo_theme/
    ├── __init__.py
    ├── locale
    │   ├── de
    │   |   └── LC_MESSAGES
    │   |        ├── django.mo
    │   |        └── django.po
    │   └── fr
    │       └── LC_MESSAGES
    │           ├── django.mo
    │           └── django.po
    ├── static
    │   └── core
    └── templates
        └── core
            └── your_template.html
    ```
