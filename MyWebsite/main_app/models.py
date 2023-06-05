from django.db import models

# Create your models here.
class Project(models.Model):
    title_project = models.CharField(max_length = 200)
    description_project = models.TextField()
    ison_project = models.CharField(max_length = 200, default = "bx-brain")
