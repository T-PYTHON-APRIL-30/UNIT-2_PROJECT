from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.png")