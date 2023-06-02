from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=2084)
    about_course = models.TextField()
    image = models.ImageField(upload_to="images/")
