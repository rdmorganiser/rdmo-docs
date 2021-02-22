# Project settings

## Nested projects

With RDMO 1.5, projects can be nested. If this feature is not desired, the UI elements to create a project hierarchy can be disabled using:

```python
NESTED_PROJECTS = False
```

## Project file quota

The size of files which can be uploaded for a project is limited (default: 10 MB). This can setting can be changed, e.g.:

```python
PROJECT_FILE_QUOTA = '100Gb'
```

## Project import and export plugins

Project import and export plugins are described [here](/configuration/plugins.html).

## Project invitations

Project invitation settings are described [here](/configuration/email.html).
