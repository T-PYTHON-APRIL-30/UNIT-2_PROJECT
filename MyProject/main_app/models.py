from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300, null=True)
    heading1 = models.CharField(max_length=300, null=True)
    articl1 = models.TextField(null=True)
    heading2 = models.CharField(max_length=300,null=True)
    articl2 = models.TextField(null=True)
    publish_date = models.DateField()
    main_image = models.ImageField(upload_to="images/", default="images/default.jpg")
    article_image1 = models.ImageField(upload_to="images/", default="images/default.jpg")
    article_image2 = models.ImageField(upload_to="images/", default="images/default.jpg")


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField()


