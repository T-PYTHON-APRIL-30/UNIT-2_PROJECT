from django.db import models

# Create your models here.

# Courses
class Course(models.Model):
    presented_by = models.CharField(max_length=2084)
    title = models.CharField(max_length=2084)
    about_course = models.TextField()
    image = models.ImageField(upload_to="images/")
    course_hours = models.IntegerField()
    start_from = models.DateField()
    end_at = models.DateField()

# Projects 
class Project(models.Model):
    title = models.CharField(max_length=2084)
    platform = models.CharField(max_length=2084)
    project_logo = models.ImageField(upload_to="images/", default="images/default.jpg")
    about_project = models.TextField()
    project_source = models.CharField(max_length=2084,default="")

class Image(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    images = models.ImageField(upload_to="images/",default="images/default.jpg")