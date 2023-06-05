from django.db import models

# Create your models here.
class CvFile(models.Model):
    cv_file = models.FileField(upload_to = "pdf/")


class Project(models.Model):
    title_project = models.CharField(max_length = 200)
    description_project = models.TextField()
    ison_project = models.CharField(max_length = 200, default = "bx-brain")
    image_project = models.ImageField(upload_to = "img/", default="img/deep_learning.jpg")
