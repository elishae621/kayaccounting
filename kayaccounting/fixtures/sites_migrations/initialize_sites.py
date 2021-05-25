from __future__ import unicode_literals
from django.db import migrations


def insert_sites(apps, schema_editor):
    """Populate the sites model"""
    Site = apps.get_model('sites', 'Site')
    Site.objects.all().delete()

    # Register SITE_ID = 1
    Site.objects.create(domain='kayaccountingclinic.com', name='www')


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_site'),
    ]

    operations = [
        migrations.RunPython(insert_sites)
    ]
