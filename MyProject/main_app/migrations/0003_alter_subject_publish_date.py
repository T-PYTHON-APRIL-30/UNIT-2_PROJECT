# Generated by Django 4.2.1 on 2023-06-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_image_subject_main_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='publish_date',
            field=models.DateField(),
        ),
    ]
