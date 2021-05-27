# configuration for logger 
import json
import logging
import os
from kayaccounting.settings.components import conf_location

with open(conf_location) as config_json:
    config = json.load(config_json)


FORMAT = '%(asctime)s %(levelname)-%s ' \
'%(threadName)-14s (%(pathname)s:%(lineno)d) ' \
'%(name)s.%(function)s: %(message)s'

LOGGING = {
  'version': 1,
  'disable_exiting_loggers': False,
  
  'formatters': {
    'my_formatter': {
      'format': FORMAT,
      #'style': '%',
      #'class': 'kayaccounting.logging_helpers.HostnameAddingFormatter',
    },
  },
  
  'handlers': {
    'default': {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': BASE_DIR / 'logs/default.log',
        'maxBytes': 1024*1024*5,
        'backupCount': 5,
        'formatter': 'my_formatter',
    },
    'request_handler': {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': BASE_DIR / 'logs/django_request.log',
        'maxBytes': 1024*1024*5,
        'backupCount': 5,
        'formatter': 'my_formatter',
    },
    'mail_admins': {
      'level': 'ERROR', 
      'class': 
        'django.utils.log.AdminEmailHandler',
      'include_html': True,
    },
    'console': {
      'class': 'logging.StreamHandler', 
      'formatter': 'my_formatter',
    },
  },
  
  'loggers': {
      # root logger 
      '': {
        'level': config.get('ROOT_LOG_LEVEL', 'INFO'),
        'handlers': ['console', 'mail_admins', 'default'],
      },
      'django': {
        'handlers': ['console', 'mail_admins', 'default'],
        'level': config.get('DJANGO_LOG_LEVEL', 'INFO'),
        'propagate': False,
      },
      'django.request': {
        'handlers': ['request_handler'],
        'level': 'DEBUG',
        'propagate': False
      },
      'django.server': {
        'propagate': True,
      },
  },
  
}