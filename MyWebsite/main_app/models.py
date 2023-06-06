from django.db import models

# Create your models here.
class CvFile(models.Model):
    cv_file = models.FileField(upload_to = "pdf/")


class Project(models.Model):
    title_project = models.CharField(max_length = 200)
    description_project = models.TextField()
    ison_project = models.CharField(max_length = 200, default = "bx-brain")
    image_project = models.ImageField(upload_to = "img/", default="img/deep_learning.jpg")

    def __str__(self):
        return self.title_project


class Education(models.Model):
    degree = models.CharField(max_length = 200)
    field = models.CharField(max_length = 200)
    university = models.CharField(max_length = 200)
    description_education = models.TextField()

    def __str__(self):
        return self.field


class Experience(models.Model):
    job = models.CharField(max_length = 200)
    co = models.CharField(max_length = 200)
    description_experience = models.TextField()

    def __str__(self):
        return self.job


class Skills(models.Model):
    name_skill = models.CharField(max_length = 200)
    percent_skill = models.CharField(max_length =200)

    def __str__(self):
        return self.name_skill


class Courses(models.Model):
    name_course = models.CharField(max_length = 200)
    place_course = models.CharField(max_length =200)
    field_course = models.CharField(max_length =200, default = "Computer security")

    def __str__(self):
        return self.name_course
