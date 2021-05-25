"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings 
default environment is 'development'.
To change settings file:
'DJANGO_ENV=production python manage.py runserver'
"""

from split_settings.tools import optional, include 
from os import environ

ENV = environ.get('DJANGO_ENV')

base_settings = [
    'components/common.py',     # standard django settings
    'components/database.py',   # postgres
    'components/emails.py',     # smtp
    # 'components/constance.py',  # django-constance configurations

    # You can even use glob: 
    # 'components/*.py',

    # Select the right env:
    'environments/{0}.py'.format(ENV),
    
    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)