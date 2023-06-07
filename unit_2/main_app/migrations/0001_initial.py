# Generated by Django 4.2.1 on 2023-06-07 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies_TV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('description', models.TextField()),
                ('imdb_rating', models.FloatField()),
                ('type', models.TextField()),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('release_date', models.DateField()),
            ],
        ),
    ]
