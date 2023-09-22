# Configuration

The RDMO application uses the [Django settings](https://docs.djangoproject.com/en/4.2/topics/settings/) module for its configuration, all of the default settings are defined in [rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/settings.py). A deployed instance of RDMO uses the following settings module as its main configuration:

```
config/settings/local.py
```
This `local.py` module is copied from the template `config/settings/sample.local.py`, contained in the `rdmo-app`, during the installation process. The module is ignored by git and is meant to contain your local adjustments and secret information (e.g. database connections).  
The `config/settings/local.py` module can be used to override all of the default settings of RDMO (see: [rdmo/core/settings.py](https://github.com/rdmorganiser/rdmo/blob/master/rdmo/core/settings.py)).


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
