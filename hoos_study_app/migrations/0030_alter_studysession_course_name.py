# Generated by Django 4.2.16 on 2024-12-05 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoos_study_app', '0029_alter_studysession_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studysession',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoos_study_app.course'),
        ),
    ]
