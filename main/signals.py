from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from kayaccounting.settings.components import conf_location
from main.models import ContactMessage
from django.conf import settings


import json
with open(conf_location) as config_json:
    config = json.load(config_json)

@receiver(post_save, sender=ContactMessage)
def notify_me_of_registration(sender, instance, created, **kwargs):
    if created:
        title = 'someone has sent a message'
        text_message = "check the site and reply the user asap"
        from_email = config['MAIL_USERNAME']
        to_email = settings.ADMINS
        msg = EmailMultiAlternatives(
            title, text_message, from_email, to_email)
        msg.send(fail_silently=True)


@receiver(post_save, sender=ContactMessage)
def send_confirmation_for_message(sender, instance, created, **kwargs):
    if created:
        title = 'Kay Accounting Clinic'
        text_message = "Thank you for your interest in Kay Accounting Clinic.\n\nThis is to acknowledge receipt of your e-mail. Where applicable, a reply will be sent to you as soon as possible.\n\nRegards."
        from_email = config['MAIL_USERNAME']
        to_email = [instance.email]
        msg = EmailMultiAlternatives(
            title, text_message, from_email, to_email)
        msg.send(fail_silently=True)
