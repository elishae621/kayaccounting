from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import ContactMessage, Mail, Subscriber
from django.conf import settings
# from .tasks import async_notify_of_registration, async_auto_reply_contactMessage
from django.core.mail import EmailMultiAlternatives


import json
with open(settings.BASE_DIR / 'kay_config.json') as config_json:
    config = json.load(config_json)


@receiver(post_save, sender=Subscriber)
def notify_me_of_registration(sender, instance, created, **kwargs):
    if created:
        # async_notify_of_registration.delay()
        title = 'someone has added their email to KayaccountingClinic'
        text_message = f"{instance.email} has been added to the site"
        from_email = config['MAIL_USERNAME']
        to_email = config['CLIENT']
        msg = EmailMultiAlternatives(
            title, text_message, from_email, [to_email])
        return msg.send(fail_silently=True)


@receiver(post_save, sender=Subscriber)
def auto_reply_contactMessage(sender, instance, created, **kwargs):
    if created:
        # async_auto_reply_contactMessage.delay(instance.email)
        title = 'Kay Accounting Clinic'
        text_message = "Thank you for your interest in Kay Accounting Clinic.\n\nPlease tell us more about how we can serve you by replying to this mail\n\nRegards."
        from_email = config['MAIL_USERNAME']
        to_email = [instance.email]
        msg = EmailMultiAlternatives(
            title, text_message, from_email, to_email)
        return msg.send(fail_silently=True)


@receiver(post_save, sender=Mail)
def send_custom_mail(sender, instance, created, **kwargs):
    from_email = config['MAIL_USERNAME']
    to_email = instance.email
    msg = EmailMultiAlternatives(
        instance.subject, instance.content, from_email, [to_email])
    msg.send(fail_silently=False)