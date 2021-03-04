from core.settings import DEBUG, BASE_DIR

LOG_PATH = BASE_DIR / 'core/log'

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'filters': {
            'special': {
                '()': 'core.log.SpecialFilter',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['special']
            },
            'file_info': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': f'{LOG_PATH}/info.log',
                'formatter': 'verbose'
            },
            'file_auth': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename':  f'{LOG_PATH}/auth.log',
                'formatter': 'verbose'
            },
            'file_services': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': f'{LOG_PATH}/services.log',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'core.custom': {
                'handlers': ['console', 'mail_admins', 'file_info'],
                'level': 'INFO',
                'filters': ['special']
            },
            'core.auth': {
                'handlers': ['console', 'file_auth'],
                'level': 'INFO',
                'filters': ['special']
            },
            'core.services': {
                'handlers': ['console', 'file_services'],
                'level': 'INFO',
                'filters': ['special']
            }
        }
    }
