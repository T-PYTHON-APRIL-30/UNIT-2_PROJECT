# Generated by Django 4.2.1 on 2023-06-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='Juhaina', max_length=500),
        ),
    ]
