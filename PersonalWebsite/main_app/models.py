from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()