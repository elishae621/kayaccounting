"""
configuration for database 
"""

from kayaccounting.settings.components import config 

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kayaccounting',
        'USER': 'adminuser',
        'PASSWORD': config['DATABASE_PASSWORD'],
        'HOST': '127.0.0.1',
        'POST': '5432',
    }
}
