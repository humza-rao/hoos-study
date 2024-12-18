# Generated by Django 4.2.16 on 2024-10-19 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoos_study_app', '0009_alter_studysession_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studysessionlocation',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Study Session Location'),
        ),
        migrations.CreateModel(
            name='StudySessionAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('available_start', models.DateTimeField(verbose_name='Start Availability')),
                ('available_end', models.DateTimeField(verbose_name='End Availability')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoos_study_app.studysession')),
            ],
        ),
    ]