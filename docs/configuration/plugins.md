# Plugins

```eval_rst
.. warning::
    This is an advanced feature of RDMO.
```

Plugins can be used to customize or extend specific actions in RDMO using custom Python code outside of the centrally maintained code base. This can be used to perform actions which are specific to a RDMO instance. With the possibility to add code to RDMO comes the danger of introducing additional bugs and security issues. Please be extra careful when using this **advanced** feature.

Plugins are created by implementing Python classes (e.g. in the local RDMO app), and register them in the `config/settings/local.py` file. These classes need to inherit from prepared base classes in the RDMO source code.

As of now the following plugins can be created:

-	Project exports (from `rdmo.projects.export.Export`\)
-	Project imports (from `rdmo.projects.imports.Import`\)

To be usable by RDMO, the plugins need to be available in the virtual environment in which RDMO is running. There are severeal possibilities to archive this, but we suggest to use one of the following:

1.	If only the plugins provided in [rdmo-catalog](https://github.com/rdmorganiser/rdmo-plugins) should be used and no modifications are desired, they can be directly installed from GitHub using:

	```bash
	pip install git+https://github.com/rdmorganiser/rdmo-plugins
	```

2.	If you intent to write plugins yourself or if you want to modify plugins, you should create a python module in your `rdmo-app`, which is just a directory containing an empty `__ini__.py` file. Python files in this directory are then automatically available to your RDMO instance.

	```bash
	mkdir my_plugins
	touch my_plugins/__init__.py
	# place, e.g., madmp.py in my_plugins/
	```

As a last step, the plugins need to registered in `config/settings/local.py`. The setting depends on the class of plugin and is described below.

## Project export plugins

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

Please refer to https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/exports.py for the default project export plugins and code examples. The code which uses the plugin is located in https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/views.py (`ProjectExportView`).

## Project import plugins

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

Please refer to https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/imports.py for the default project import plugins and code examples. The code which uses the plugin is located in https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/views.py (`ProjectCreateUploadView`, `ProjectCreateImportView`, `ProjectUpdateUploadView`, `ProjectUpdateImportView`).

## Examples of how to install

We will mention two possibilities of how to install [rdmo-plugins](https://github.com/rdmorganiser/rdmo-plugins). Depending on your use case you should pick the one that fits you more. The first one using `pip` does a good job if you are just planning to use the plugins from the repo without modifying these. The other method requires to copy the necessary python files into your local app folder which has advantages if you are planning to modify existing or create your own plugins.

Please note that the imports require Django's translation utils and that usually use these with an underscore. If you are getting import errors please check if you have the following line at the beginning of your `local.py`.

```python
from django.utils.translation import ugettext_lazy as _
```

### Use pip

To install directly from github simply run

```shell
pip install git+https://github.com/rdmorganiser/rdmo-plugins
```

Afterwards you need to configure the plugins you are willing to use in your `local.py`. Here is an example of how to add different export formats. The three strings in brackets configure the url under which the export will be available, the name of the entry in the export menu and the path from where to import the plugin. The path resembles the structure in the `rdmo plugins` repository. If you look into it you will find the files containing the imported classes mentioned below. At the beginning of the path you use `rdmo_plugins` because you added `rdmo-plugins` to your installed python libraries. The dash is replaced by an underscore because python is not very fond of dashes when it comes to imports.

```python
PROJECT_EXPORTS.append(('madmp', _('as madmp'), 'rdmo_plugins.exports.madmp.MaDMPExport'))
PROJECT_EXPORTS.append(('datacite', _('as datacite'), 'rdmo_plugins.exports.datacite.DataCiteExport'))
PROJECT_EXPORTS.append(('radar', _('as radar'), 'rdmo_plugins.exports.radar.RadarExport'))
```

### Copy files

The other method we recommend when you are planning to modify the plugins or create your own ones is to simply copy the python files into your local app folder. Let's say you create a subfolder `plugins` containing another folder `exports` in your app directory. Then you copy the `madmp.py` from the `rdmo-plugins` into `exports`. Having done this you can import this file in your local app without specifying a module path. It is found by the importer as it resides in your rdmo app folder. Your import lines in the `local.py` would look like this:

```python
PROJECT_EXPORTS.append(('madmp', _('as madmp'), 'plugins.exports.datacite.DataCiteExport'))
```
