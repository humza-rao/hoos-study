# Generated by Django 4.2.16 on 2024-10-18 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoos_study_app', '0007_studysession_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studysession',
            old_name='data',
            new_name='date',
        ),
    ]