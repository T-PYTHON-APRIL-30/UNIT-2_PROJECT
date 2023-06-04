from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    mobile = models.IntegerField(max_length=10)
    message = models.TextField(max_length=1024)
