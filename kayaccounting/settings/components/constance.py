"""
Dynamic settings for django application 
using Django Constance
https://github.com/jazzband/django-constance/
"""
from django.conf import settings 

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'NAME': ('kayaccounting', 'Name of the application'),
    
    'COMPLETED_PROPERTY': (20500, 'Number of completed property'),
    'PROPERTY_SALES': (7600, 'Number of properties sold'),
    'APARTMENT_RENT': (12300, 'Number of apartments rented out'),
    'HAPPY_CLIENTS': (15200, 'Number of happy clients'),

    'HEADER': (1, 'Type of header and hero banner to use, valid inputs are 1 to 8'),
    'EXPLORE_PROPERTY': (True, 'show explore property block in homepage'),
    'PROPERTY_LOCATION': (True, 'show property location block in homepage'),
    'ACHIEVEMENT': (True, 'show achievement block in homepage'),
    'RECENT_RENT_PROPERTY': (True, 'show latest property block in homepage'),
    'LATEST_SALE_PROPERTY': (True, 'show all property block in homepage'),
    'HOW_IT_WORKS': (True, 'show how it works block in homepage'),
    'FEATURED_AGENTS': (True, 'show featured agents block in homepage'),
    'REVIEWS': (True, 'show testimonals block in homepage'),
    'BLOG_GRID': (True, 'show blog grid block in homepage'),
    'PRICE_TABLE': (True, 'show price table in homepage'),
    'DOWNLOAD_APP': (True, 'show download app in homepage'),
    'CALL_TO_ACTION': (True, 'show call to action in homepage'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'General Options': {
        'fields': (
            'NAME',
        ),
        'collapse': True
    },
    'Home Page': {
        'fields': (
            'HEADER',
            'EXPLORE_PROPERTY',
            'PROPERTY_LOCATION',
            'ACHIEVEMENT',
            'RECENT_RENT_PROPERTY',
            'LATEST_SALE_PROPERTY',
            'HOW_IT_WORKS',
            'FEATURED_AGENTS',
            'REVIEWS',
            'BLOG_GRID',
            'PRICE_TABLE',
            'DOWNLOAD_APP',
            'CALL_TO_ACTION',
        ),
        'collapse': True 
    },
    'Achievements': {
        'fields': (
            'COMPLETED_PROPERTY',
            'PROPERTY_SALES',
            'APARTMENT_RENT',
            'HAPPY_CLIENTS',
        ),
        'collapse': True 
    }
}
