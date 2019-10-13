# Logging

Logging in Django can be very complex and is covered extensively in the [Django documentation](https://docs.djangoproject.com/en/stable/topics/logging/). For a suitable logging of RDMO you can add the following to your `config/settings/local.py`:

```python
iimport os

LOG_LEVEL = 'DEBUG'
LOG_DIR = '/var/log/rdmo/'  # this directory needs to be writable by the rdmo user
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s'
        },
        'name': {
            'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'error_log': {
            'level': 'ERROR',
            'class':'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default'
        },
        'ldap_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'ldap.log'),
            'formatter': 'name'
        },
        'rules_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'rules.log'),
            'formatter': 'name'
        },
        'rdmo_log': {
            'level': 'DEBUG',
            'class':'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'rdmo.log'),
            'formatter': 'name'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'error_log'],
            'level': 'ERROR',
            'propagate': True
        },
        'django_auth_ldap': {
            'handlers': ['ldap_log'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'rules': {
            'handlers': ['rules_log'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'rdmo': {
            'handlers': ['rdmo_log'],
            'level': LOG_LEVEL,
            'propagate': True
        }
    }
}
```

This produces several logs:

* `/var/log/rdmo/error.log` will contain exception messages from application errors (status code: 500). The message is the same that is shown when `DEBUG = True`, which should not be the case in a production environment. In addition to the log entry, an E-mail is send to all admins specified in the `ADMINS` setting.
* `/var/log/rdmo/rdmo.log` will contain additional logging information from the RDMO code.
* `/var/log/rdmo/ldap.log` and `/var/log/rdmo/rules.log` can be used to debug the LDAP authentication or the internal permission system.
