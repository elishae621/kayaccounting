from django.db.models.signals import post_save
from django.dispatch import receiver
try:
  from kayaccounting.settings.components import conf_location
except ImportError:
  conf_location = '/etc/kayaccounting.json'
from main.models import ContactMessage
from django.conf import settings
from .tasks import async_notify_of_registration, async_auto_reply_contactMessage

import json
with open(conf_location) as config_json:
    config = json.load(config_json)


@receiver(post_save, sender=ContactMessage)
def notify_me_of_registration(sender, instance, created, **kwargs):
    if created:
        async_notify_of_registration.delay()
        

@receiver(post_save, sender=ContactMessage)
def auto_reply_contactMessage(sender, instance, created, **kwargs):
    if created:
        async_auto_reply_contactMessage.delay(instance.email)