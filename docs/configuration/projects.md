# Project settings

## Auto-Save

By default, users need to save their input in the interview explicitly using the save button. This behavior can be changed adding the `PROJECT_QUESTIONS_AUTOSAVE` entry to your configuration.

```python
PROJECT_QUESTIONS_AUTOSAVE = True
```

With this setting, all input **except typing into text or text area fields** will be saved on the server immediately. This comprises, e.g. using the Navigation, radio buttons, check boxes.

## Project tasks and views

Before RDMO 1.6, tasks and views were completely hidden from the user, if no tasks or views have been configured. Now, interface elements are displayed regardless. If you don't need tasks and/or views in your RDMO instance, they can be hidden using:

```python
PROJECT_ISSUES = False
PROJECT_VIEWS = False
```

## Sending tasks

Sending tasks from projects is described [in the section on email](/configuration/email.html#send-tasks-via-email).

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

Project import and export plugins are described [in the chapter on plugins](/plugins/index.html).

## Project invitations

Project invitation settings are described [in the section on email](/configuration/email.html#invite-users-to-projects).
