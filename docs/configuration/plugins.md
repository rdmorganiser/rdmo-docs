Plugins
=======

```eval_rst
.. warning::
    This is an advanced feature of RDMO.
```

Pluigins can be used to customize or extend specific actions in RDMO using custom Python code outside of the centrally maintained code base. This can be used to perform actions which are specific to a RDMO instance. With the possibility to add code to RDMO comes the danger of introducing additional bugs and security issues. Please be extra careful when using this **advanced** feature.

Plugins are created by implementing Python classes (e.g. in the local RDMO app), and register them in the `config/settings/local.py` file. These classes need to inherit from prepared base classes in the RDMO source code.

As of now the following plugins can be created:

* Project exports (from `rdmo.projects.export.Export`)
* Project imports (from `rdmo.projects.imports.Import`)

To be usable by RDMO, the plugins need to be available in the virtual environment in which RDMO is running. There are severeal possibilities to archive this, but we suggest to use one of the following:

1. If only the plugins provided in [rdmo-catalog](https://github.com/rdmorganiser/rdmo-plugins) should be used and no modifications are desired, they can be directly installed from GitHub using:

    ```bash
    pip install git+https://github.com/rdmorganiser/rdmo-plugins
    ```

2. If you intent to write plugins yourself or if you want to modify plugins, you should create a python module in your `rdmo-app`, which is just a directory containing an empty `__ini__.py` file. Python files in this directory are then automatically available to your RDMO instance.

    ```bash
    mkdir my_plugins
    touch my_plugins/__init__.py
    # place, e.g., madmp.py in my_plugins/
    ```

As a last step, the plugins need to registered in `config/settings/local.py`. The setting depends on the class of plugin and is described below.


Project export plugins
----------------------

Custom project exports can be created by implementing a class inheriting `rdmo.projects.export.Export`. They can be used to create a custom export format, to be selected by the users to download an export of their project data.

The Plugin class needs to implement a `render()` function which takes no arguments and returns a `django.http.HttpResponse`. The export can be created from `self.project`, `self.snapshot` and `self.values` instance variables.

The export plugin needs to be added to the `PROJECT_EXPORTS` in `config/settings/local.py`. The default settings are:

```python
PROJECT_EXPORTS = [
    ('xml', _('as RDMO XML'), 'rdmo.projects.exports.RDMOXMLExport'),
    ('csvcomma', _('as CSV (comma separated)'), 'rdmo.projects.exports.CSVCommaExport'),
    ('csvsemicolon', _('as CSV (semicolon separated)'), 'rdmo.projects.exports.CSVSemicolonExport'),
]
```

In order to use the plugins in [rdmo-catalog](https://github.com/rdmorganiser/rdmo-plugins), add the following to your `config/settings/local.py`:

```python
PROJECT_EXPORTS = [
    ('xml', _('as RDMO XML'), 'rdmo.projects.exports.RDMOXMLExport'),
    ('csvcomma', _('as CSV (comma separated)'), 'rdmo.projects.exports.CSVCommaExport'),
    ('csvsemicolon', _('as CSV (semicolon separated)'), 'rdmo.projects.exports.CSVSemicolonExport'),
    ('madmp', _('as maDMP JSON'), 'rdmo_plugins.exports.madmp.MaDMPExport'),
    ('datacite', _('as DataCite XML'), 'rdmo_plugins.exports.datacite.DataCiteExport'),
    ('radar', _('as RADAR XML'), 'rdmo_plugins.exports.radar.RadarExport')
]
```

Please refer to <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/exports.py> for the default project export plugins and code examples. The code which uses the plugin is located in <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/views.py> (`ProjectExportView`).


Project import plugins
----------------------

Similarly, custom project imports can be created implementing a class inheriting `rdmo.projects.imports.Import`. They can be used to import project data from files which are uploaded by the user.

The Plugin class needs to implement a `check()` function which takes no arguments and only returns `True` if an uploaded file can be imported by this plugin. The `self.file_name` instance variable can be used for this. In most cases, this will include opening and parsing the file.

In addition, a `process()` needs to be implemented which which takes no arguments and returns `None`, but extracts the data from the file and populates the `self.project`, `self.catalog`, `self.values`, `self.snapshots`, `self.tasks` and `self.views` instance variables.

The import plugin needs to be added to the `PROJECT_IMPORTS` in `config/settings/local.py`. The default settings are:

```python
PROJECT_IMPORTS = [
    ('xml', _('from RDMP XML'), 'rdmo.projects.imports.RDMOXMLImport'),
]
```

In order to use the plugins in [rdmo-catalog](https://github.com/rdmorganiser/rdmo-plugins), add the following to your `config/settings/local.py`:

```python
PROJECT_IMPORTS = [
    ('xml', _('from RDMP XML'), 'rdmo.projects.imports.RDMOXMLImport'),
    ('madmp', _('from maDMP'), 'rdmo_plugins.imports.madmp.MaDMPImport'),
    ('datacite', _('from DataCite XML'), 'rdmo_plugins.imports.datacite.DataCiteImport'),
    ('radar', _('from RADAR XML'), 'rdmo_plugins.imports.radar.RadarImport'),
]
```

Please refer to <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/imports.py> for the default project import plugins and code examples. The code which uses the plugin is located in <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/views.py> (`ProjectCreateUploadView`, `ProjectCreateImportView`, `ProjectUpdateUploadView`, `ProjectUpdateImportView`).
