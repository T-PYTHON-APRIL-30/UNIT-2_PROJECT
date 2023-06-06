from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    is_published = models.BooleanField(default=True)
    release_date = models.DateField()


class Review(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



