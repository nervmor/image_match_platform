
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d: %(message)s'
        },
    },
    'handlers': {
        'global_file': {
             'level': 'DEBUG',
             'class': 'logging.handlers.TimedRotatingFileHandler',
             'filename': 'global.log',
             'formatter':'standard'
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'error.log',
            'formatter': 'standard'
        },
        'console':{
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'all': {
            'handlers' :['global_file', 'error_file', 'console'],
            'level':'DEBUG',
            'propagate': True
        },
    }
}