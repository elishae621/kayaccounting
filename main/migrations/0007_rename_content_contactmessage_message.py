# Generated by Django 3.2.3 on 2021-06-29 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210606_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='content',
            new_name='message',
        ),
    ]
