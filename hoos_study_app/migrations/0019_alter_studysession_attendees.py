# Generated by Django 4.2.16 on 2024-11-06 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoos_study_app', '0018_merge_20241106_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studysession',
            name='attendees',
            field=models.ManyToManyField(related_name='study_session', to=settings.AUTH_USER_MODEL),
        ),
    ]
