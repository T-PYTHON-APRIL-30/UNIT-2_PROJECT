from django.db import models


# Create your models here.

class Post(models.Model):

    type_choices = models.TextChoices("Post Type", ["Manual", "Digital","Animal","Web"])

    title = models.CharField(max_length=1000)
    description = models.TextField()
    date = models.DateField()
    size = models.CharField(max_length=1000)
    price = models.IntegerField()
    rating = models.IntegerField(default=5)
    hour = models.IntegerField(default="5")
    img = models.ImageField(upload_to="img/",default="img/pinklogo.png")
    type = models.CharField(max_length=64, choices=type_choices.choices)






class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

