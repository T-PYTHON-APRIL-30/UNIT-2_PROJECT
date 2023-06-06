from django.db import models
from datetime import date
from django import forms

# Create your models here.

class novel(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    summary = models.TextField()
    abstract = models.TextField()
    img = models.ImageField(upload_to="image/", default="defaults/Books.jpeg")
    file = models.FileField(upload_to="novels/", default=None)

class comment(models.Model):
    Novel = models.ForeignKey(novel, on_delete=models.CASCADE)
    name = models.CharField(max_length=126)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class inquiry(models.Model):
    fullname = models.CharField(max_length=1048)
    emailAddress = models.EmailField()
    type_of_inquery = models.CharField(max_length=128)
    message = models.TextField()
    file4 = models.FileField(upload_to="files/", default="defaults/Doc1.pdf")


    