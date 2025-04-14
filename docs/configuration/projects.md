# Project settings

## Project tasks and views

Before RDMO 1.6, tasks and views were completely hidden from the user, if no tasks or views have been configured. Now, interface elements are displayed regardless. If you don't need tasks and/or views in your RDMO instance, they can be hidden using:

```python
PROJECT_ISSUES = False
PROJECT_VIEWS = False
```

## Automatically synchronize tasks and views to projects

```{note}
This feature was introduced in RDMO 2.3.
```

Tasks and views can be configured to "belong" to specific catalogs. By default, this information is only used to filter the tasks and views for newly created projects. Afterwards, users can asign any task or view to any project.

Optionally, RDMO can be configured to automatically update projects when the catalog for a task or view is changed. This can be done independently for tasks and views:

```python
PROJECT_TASKS_SYNC = True
PROJECT_VIEWS_SYNC = True
```

If these settings are set, the user interface elements for changing the tasks or views in a project are hidden. 

## Sending tasks

Sending tasks from projects is described [in the section on email](/configuration/email.md#send-tasks-via-email).

## Nested projects

With RDMO 1.5, projects can be nested. If this feature is not desired, the UI elements to create a project hierarchy can be disabled using:

```python
NESTED_PROJECTS = False
```

## Visible projects

In order to make projects available to all users (e.g. to be used as a template), project can be made visible
by `site_managers` or Admins (see [Roles](/administration/users.md#roles)). This feature can be enabled using:

```python
PROJECT_VISIBILITY = True
```

Project visibility can be restricted to certain sites in a [Multisite Setup](/configuration/multisite.md) (i.e. when `MULTISITE = True`) or
groups (when `GROUP = True`).

## Project file quota

The size of files which can be uploaded for a project is limited (default: 10 MB). This can setting can be changed, e.g.:

```python
PROJECT_FILE_QUOTA = '100Gb'
```

## Project import and export plugins

Project import and export plugins are described [in the chapter on plugins](/plugins/index).

## Project invitations

Project invitation settings are described [in the section on email](/configuration/email.md#invite-users-to-projects).

## Restrict project creation

The creation of new projects can be restricted to certain groups. This is particularly useful in a scenario where users from one authentication method (e.g. LDAP) are automatically placed in the `internal` group, while users from another (e.g. ORCID) are not:

```python
PROJECT_CREATE_RESTRICTED = True
PROJECT_CREATE_GROUPS = [
    'internal'
]
```

## Project contact form

```{note}
This feature was introduced in RDMO 2.3.
```

Contact forms for each question in the interview can be used to allow the users to contact the management of the RDMO instance via email. To enable this feature use:

```
PROJECT_CONTACT = True
PROJECT_CONTACT_RECIPIENTS = [
    ('manager@example.com', 'Manni Manager <manni@example.com>'),
    ...
]
```
