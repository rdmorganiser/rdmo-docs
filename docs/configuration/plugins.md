Plugins
=======

```eval_rst
.. warning::
    This is an upcoming feature of RDMO. It is not part of the release, yet.
```

Pluigins can be used to customize or extend specific actions in RDMO using custom Python code outside of the centrally maintained code base. This can be used to perform actions which are specific to a RDMO instance. With the possibility to add code to RDMO comes the danger of introducing additional bugs and security issues. Please be extra careful when using this **advanced** feature.

Plugins are created by implementing Python classes (e.g. in the local RDMO app), and register them in the `config/settings/local.py` file. These classes need to inherit from prepared base classes in the RDMO source code. As of now the following plugin classes can be used.


Export
------

Custom project exports can be created by implementing a class inheriting `rdmo.projects.export.Export`. They can be used to create a custom export format, to be selected by the users to download an export of their project data.

The Plugin class needs to implement a `render()` function which takes no arguments and returns a `django.http.HttpResponse`. The export can be created from `self.project`, `self.snapshot` and `self.values` instance variables.

The export plugin needs to be added to the `PROJECT_EXPORTS` in `config/settings/local.py`. The default settings are:

```
PROJECT_EXPORTS = [
    ('xml', _('as RDMO XML'), 'rdmo.projects.exports.XMLExport'),
    ('csvcomma', _('as CSV (comma separated)'), 'rdmo.projects.exports.CSVCommaExport'),
    ('csvsemicolon', _('as CSV (semicolon separated)'), 'rdmo.projects.exports.CSVSemicolonExport'),
]
```

Please refer to <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/exports.py> for the default project export plugins and code examples. The code which uses the plugin is located in <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/views.py> (`ProjectExportView`).


Import
------

Similarly, custom project imports can be created implementing a class inheriting `rdmo.projects.imports.Import`. They can be used to import project data from files which are uploaded by the user.

The Plugin class needs to implement a `check()` function which takes no arguments and only returns `True` if an uploaded file can be imported by this plugin. The `self.file_name` instance variable can be used for this. In most cases, this will include opening and parsing the file.

In addition, a `process()` needs to be implemented which which takes no arguments and returns `None`, but extracts the data from the file and populates the `self.project`, `self.catalog`, `self.values`, `self.snapshots`, `self.tasks` and `self.views` instance variables.

The import plugin needs to be added to the `PROJECT_IMPORTS` in `config/settings/local.py`. The default settings are:

```
PROJECT_IMPORTS = [
    ('xml', _('from RDMP XML'), 'rdmo.projects.imports.RDMOXMLImport'),
]
```

Please refer to <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/imports.py> for the default project import plugins and code examples. The code which uses the plugin is located in <https://github.com/rdmorganiser/rdmo/blob/master/rdmo/projects/views.py> (`ProjectCreateUploadView`, `ProjectCreateImportView`, `ProjectUpdateUploadView`, `ProjectUpdateImportView`).
