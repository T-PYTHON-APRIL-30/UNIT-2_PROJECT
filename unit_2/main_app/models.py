from django.db import models

# Create your models here.


class Movies_TV(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()
    imdb_rating = models.FloatField()
    type = models.CharField(max_length=10)
    image = models.ImageField(upload_to="images/")
    release_date = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title}"


class Career(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    tasks = models.TextField()
    logo = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return f"{self.position}"
