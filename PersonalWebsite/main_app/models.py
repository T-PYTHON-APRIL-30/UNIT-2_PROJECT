from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=2000)
    description=models.TextField()
    image=models.ImageField(upload_to='images/',default='images/blog2.jpg')
    project_date=models.DateField()

class Contact(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField()
    subject=models.CharField(max_length=2000)
    content=models.TextField()


