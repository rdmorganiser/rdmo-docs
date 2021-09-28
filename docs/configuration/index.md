# Configuration

The RDMO application uses the [Django settings](https://docs.djangoproject.com/en/1.10/topics/settings) module for it's configuration. To seperate the base configuration and your local adjustments and secret information (e.g. database connections), RDMO splits the settings into two files:

-	`config/settings/base.py`, which is part of the git repository.
-	`config/settings/local.py`, which is ignored by git.

As part of the installation `config/settings/local.py` should be created from the template `config/settings/sample.local.py`.

While technically the local settings file `config/settings/local.py` can be used to override all of the settings in `config/settings/sample.local.py`, it should be used to customize the settings already available in `config/settings/sample.local.py`.

```eval_rst
----

.. toctree::
   :maxdepth: 2

   general
   databases
   email
   authentication/index
   export-formats
   cache
   logging
   projects
   multisite
```
