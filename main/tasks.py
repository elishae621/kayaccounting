import json
from celery import shared_task 
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
try:
  from kayaccounting.settings.components import conf_location
except ImportError:
  conf_location = '/etc/kayaccounting.json'

with open(conf_location) as config_json:
    config = json.load(config_json)


@shared_task
def async_notify_of_registration():
    title = 'someone has sent a message'
    text_message = "check the site and reply the user asap"
    from_email = config['MAIL_USERNAME']
    to_email = settings.ADMINS
    msg = EmailMultiAlternatives(
        title, text_message, from_email, to_email)
    return msg.send(fail_silently=True) 

@shared_task
def async_auto_reply_contactMessage(email):
    title = 'Kay Accounting Clinic'
    text_message = "Thank you for your interest in Kay Accounting Clinic.\n\nThis is to acknowledge receipt of your e-mail. Where applicable, a reply will be sent to you as soon as possible.\n\nRegards."
    from_email = config['MAIL_USERNAME']
    to_email = [email]
    msg = EmailMultiAlternatives(
        title, text_message, from_email, to_email)
    return msg.send(fail_silently=True)
