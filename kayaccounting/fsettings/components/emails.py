"""
Email configurations 
""" 

from kayaccounting.settings.components import config 

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config['MAIL_USERNAME']
EMAIL_HOST_PASSWORD = config['MAIL_PASSWORD']
DEFAULT_FROM_EMAIL = config['MAIL_USERNAME']
DEFAULT_TO_EMAIL = EMAIL_HOST_USER
