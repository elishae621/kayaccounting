from django.db import models 


class Instance(models.Model):
    email = models.EmailField(default='info@kayaccountingclinic.com')
    phone = models.CharField(max_length=22, default='+234-803-4556-488')
    address = models.CharField(max_length=100, default='some address, Lagos Nigeria')
    facebook = models.URLField(default='www.facebook.com')
    instagram = models.URLField(default='www.instagram.com')
    linkedin = models.URLField(default='www.linkedin.com')
    twitter = models.URLField(default='www.twitter.com')
    
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
