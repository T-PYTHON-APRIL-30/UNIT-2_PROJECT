# Generated by Django 4.2.1 on 2023-06-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ison_project',
            field=models.CharField(default='bx-brain', max_length=200),
        ),
    ]
