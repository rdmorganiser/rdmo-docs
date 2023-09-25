# E-Mail

RDMO needs to send E-Mails to its users. The connection to the SMTP server is configured by several settings in your `config/settings/local.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = ''
```

Here, `EMAIL_HOST` is the URL or IP of the SMTP server, `EMAIL_PORT` is the port it is listening on (usually 25, 465, or 587), and  `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are credentials, if the SMTP server needs authentication.

For a `STARTTLS` connection (usually on port 587) `EMAIL_USE_TLS` needs to be set to `True`, while `EMAIL_USE_SSL` needs to be set to `True` for an implicit TLS/SSL connection (usually on port 465).

`DEFAULT_FROM_EMAIL` sets the FROM field for the E-mails send to the users.

For a development/testing setup a simple E-mail backend, which only displays the E-mail on the terminal, can be used:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FROM = 'info@example.com'
```

This is also the default backend, if no E-mail settings are added to `config/settings/local.py`.


## Send tasks via Email

[Tasks](/management/tasks) can be send by users via email. To enable this function add the following to your `config/settings/local.py`:

```python
PROJECT_SEND_ISSUE = True

EMAIL_RECIPIENTS_CHOICES = [
    ('email@example.com', 'Eddy Example <email@example.com>'),
]
```

While `PROJECT_SEND_ISSUE` enable the feature, `EMAIL_RECIPIENTS_CHOICES` determines a fixed list of recipients for mails from your RDMO instance. Instead of a fixed list or in combination, you can also set

```python
EMAIL_RECIPIENTS_INPUT = True
```

to enable users to send tasks to arbitrary addresses. **Please consider all implications of this feature. In particular, you might not want to enable this feature, if your RDMO instance is open to anyone.** The emails will be send from the `DEFAULT_FROM_EMAIL` and set the user sending the task in CC.


## Invite users to projects

Users are invited to projects by email. If the user is already in the database, he or she will be stored with the invitation.

If not, an email will be send nevertheless and any user (usually a newly created account, but also an existing account of the user with a different email address is possible). If sending emails to non registered emails is not derisired, this feature can be prevented by setting:

```python
PROJECT_SEND_INVITE = False
```

A timeout for this process can be set with:

```python
PROJECT_INVITE_TIMEOUT = None
```
