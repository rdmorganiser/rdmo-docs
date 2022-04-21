# Configuration

The RDMO application uses the [Django settings](https://docs.djangoproject.com/en/1.10/topics/settings) module for it's configuration. RDMO uses a file:

```
config/settings/local.py
```

which is ignored by git and is meant to contain your local adjustments and secret information (e.g. database connections). As part of the installation process `config/settings/local.py` should be created from the template `config/settings/sample.local.py`. (Most of the Django configuration you might know from other projects is located in [rdmo/rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/settings.py) of the rdmo package repository.)

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
