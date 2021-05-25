"""
This file contains all the settings that defines 
the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

from typing import List 

from kayaccounting.settings.components import config 
from kayaccounting.settings.components.common import (
    INSTALLED_APPS,
    MIDDLEWARE,
)

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = [ 
    config['DOMAIN_NAME'],
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '[::1]',
]

# Installed apps for development only:

INSTALLED_APPS += (
    # Better debug:
    'debug_toolbar',
    
    # django-extra-checks:
    'extra_checks',
)

# internal_ips for debug_toolbar 
INTERNAL_IPS = [ 
    '127.0.0.1',
]


# Static files:
# httpsL//docs.djangoproject.com/en/3.2/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS: List[str] = []


MIDDLEWARE += ()


# django-extra-checks 
# https://github.com/kalekseev/django-extra-checks/

EXTRA_CHECKS = {
    'checks': [
        # Forbid 'unique_together':
        'no-unique-together',

        # Require non empty 'upload_to' argument:
        'field-file-upload-to',
        # Use the indexed option instead:
        'no-index-together',

        # Each model must be registered in admin:
        'model-admin',
        # FileField/ImageField must have non empty 'upload_to' argument:
        'field-file-upload-to',

        # Text fields shouldn't use 'null=True':
        'field-text-null',
        # Prefer using BooleanField(null=True) instead of NullBooleanField:
        'field-boolean-null',
        # Don't pass 'null=Flase' to model fileds (this is django default)
        'field-null',
        # ForeignKey fields must specify db_index explicitly if used in 
        # other indexed:
        {'id': 'field-foreign-key-db-index', 'when': 'indexes'},
        # If field nullable '(null=True)',
        # then default=None argument is redundant and should be removed:
        'field-default-null',
        # Fields with choices must have companion CheckConstraint
        # to enforce choices on database level 
        'field-choices-constraint',
    ],
}
