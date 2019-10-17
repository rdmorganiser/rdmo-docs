# Setup the application

## Basic setup
To set up the application, create a new file `config/settings/local.py` in your cloned `rdmo-app` directory. For the example user with the home `/srv/rdmo`, this would now be `/srv/rdmo/rdmo-app/config/settings/local.py`.

You can use `config/settings/sample.local.py` as template, i.e.:

```bash
cp config/settings/sample.local.py config/settings/local.py    # on Linux or macOS
copy config\settings\sample.local.py config\settings\local.py  # on Windows
```

Most of the settings of your RDMO instance are specified in this file. The different settings are explained in detail [later in the documentation](../configuration/index.html). For a minimal configuration, you need to set `DEBUG = True` to see verbose error messages and serve static files, and `SECRET_KEY` to a long random string, which you will keep secret. Your database connection is configured using the `DATABASES` variable. Database configuration is covered [later in the documentation](../configuration/databases.html). If no `DATABASE` setting is given `sqlite3` will be used as database backend.

Then, initialize the application, using:

```bash
python manage.py migrate                # initializes the database
python manage.py setup_groups           # creates groups with different permissions
python manage.py createsuperuser        # creates the admin user
```

## Third party vendor files
By default third party vendor files (like jQuery or Bootstrap javascripts) are retrieved from the content delivery networks that they are hosted on. If you would like to aviod third party requests you could host them yourself. This can be achieved easily with two simple steps.

1. download the vendor files from the cdns by running the provided script
    ```python
    python manage.py download_vendor_files
    ```

2. make sure your `local.py` does contain the following line
    ```python
    VENDOR_CDN = False
    ```

## RDMO development server

After these steps, RDMO can be run using Djangos intergrated development server:
```bash
python manage.py runserver
```

Then, RDMO is available on http://127.0.0.1:8000 in your (local) browser. The different ways RDMO can be deployed are covered in the next chapter. The newly installed RDMO instance is still empty, i.e. no questionaire or views are available. They need to be [imported](../management/export.html) and/or created as described under [Management](../management/index.html).
