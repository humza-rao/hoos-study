# Generated by Django 4.2.16 on 2024-10-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoos_study_app', '0009_alter_user_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.CharField(choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')], default='1', max_length=1),
        ),
    ]