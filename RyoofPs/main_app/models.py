from django.db import models


# # Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    send_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
