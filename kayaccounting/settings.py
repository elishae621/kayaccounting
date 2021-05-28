"""
Django settings for kayaccounting project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import json
from pathlib import Path, PurePath
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
with open(BASE_DIR / 'kay_config.json') as config_json:
    config = json.load(config_json)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['kayaccountingclinic.com', 'www.kayaccountingclinic.com',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    'widget_tweaks',

    'main.apps.MainConfig',
]


# internal_ips for debug_toolbar
INTERNAL_IPS = [
    '127.0.0.1',
    '139.162.137.57',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'main.middleware.AddConfigToAllContext',
]

ROOT_URLCONF = 'kayaccounting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kayaccounting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kayaccounting$default',
        'USER': 'kayaccounting',
        'PASSWORD': config['DATABASE_PASSWORD'],
        'HOST': 'kayaccounting.mysql.pythonanywhere-services.com',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = PurePath.joinpath(BASE_DIR, 'static')
STATIC_URL = '/static/'


MEDIA_ROOT = PurePath.joinpath(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Migration for Django Site Framework
MIGRATION_MODULES = {
    'sites': 'kayaccounting.fixtures.sites_migrations',
}

# Email smtp settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config['MAIL_USERNAME']
EMAIL_HOST_PASSWORD = config['MAIL_PASSWORD']
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = EMAIL_HOST_USER



DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'



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


# Celery settings

CELERY_BROKER_URL = 'redis://localhost:6379/0'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = "Africa/Lagos"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60



# Migration for Django Site Framework
MIGRATION_MODULES = {
    'sites': 'kayaccounting.fixtures.sites_migrations',
}


# others
ADMINS = [('Elisha', 'elishae621@gmail.com'),]


# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/kayaccounting/kayaccounting/logs/default.log',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/kayaccounting/kayaccounting/logs/django_request.log',
        },
        'server_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/kayaccounting/kayaccounting/logs/django_server.log',
        },
        'template_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/kayaccounting/kayaccounting/logs/django_template.log',
        },
        'database_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/kayaccounting/kayaccounting/logs/django_database.log',
        },
        'security_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/kayaccounting/kayaccounting/logs/django_security.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['server_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['template_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'django.db.backends': {
        #     'handlers': ['database_handler'],
        #     'level': 'ERROR',
        #     'propagate': True,
        # },
        'django.security': {
            'handlers': ['security_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },

}

