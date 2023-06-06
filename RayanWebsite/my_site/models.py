from django.db import models

# Create your models here.

class message(models.Model):
    name= models.CharField(max_length=150)
    email= models.TextField()
    title= models.CharField(max_length=200)
    content= models.TextField()
    send_date= models.DateTimeField(auto_now_add=True)