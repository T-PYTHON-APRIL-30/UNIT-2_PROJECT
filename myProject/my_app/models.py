from django.db import models

# Create your models here.

class ContactMe(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=254)
    message=models.TextField()

class Comment(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
