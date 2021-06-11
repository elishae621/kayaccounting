from django.db import models
from .utils import current_time


class Instance(models.Model):
    email = models.EmailField(default='info@kayaccountingclinic.com')
    phone = models.CharField(max_length=22, default='+2347011540697')
    address = models.CharField(max_length=100, default='some address, Lagos Nigeria')
    facebook = models.URLField(default='https://www.facebook.com', help_text="Add http or https to the url")
    instagram = models.URLField(default='https://www.instagram.com', help_text="Add http or https to the url")
    linkedin = models.URLField(default='https://www.linkedin.com', help_text="Add http or https to the url")
    twitter = models.URLField(default='https://www.twitter.com', help_text="Add http or https to the url")

    class Meta:
        verbose_name = 'Kay Accounting'
        verbose_name_plural = 'Kay Accounting'


class ContactMessage(models.Model):
    class MessageStatus(models.TextChoices):
        NEW = 'NEW'
        WAITING = 'WAITING'
        FINISHED = 'FINISHED'

    name = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15, choices=MessageStatus.choices, default=MessageStatus.NEW)

    def __str__(self):
        return f'{self.name} on {self.date}'

    class Meta:
        constraints = [
            models.CheckConstraint(name="main_ContactMessage_status_valid",
            check=models.Q(status__in=["NEW", "WAITING", "FINISHED"])),
        ]



class Mail(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    date_sent = models.DateTimeField(default=current_time)

    def __str__(self):
        return f"{self.email} on {self.date_sent}"


class Subscriber(models.Model):
    email = models.EmailField()