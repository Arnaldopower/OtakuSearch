from django.contrib.auth.models import AbstractUser
from django.db import models


# This is an example of a model in Django so that you can see how you can define your own models :D
# DON'T FORGET to run `python manage.py makemigrations` and `python manage.py migrate` after changing this file!!!


class Manga(models.Model): #Matias
    pass


class Author(models.Model): #Angel
    pass


class Status(models.Model): #Oscar
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class Adaptations(models.Model): #Joel
    pass

class Anime(models.Model): #Oscar
    name = models.CharField(max_length=150)
    seasons = models.IntegerField()
    description = models.CharField(max_length=500)
    cover = models.URLField()
    rating = models.FloatField(min=0.0, max=1.0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class AnimeSeason(models.Model): #Arnau
    pass

class Genre(models.Model): #Joel 
    pass

class Studio(models.Model): #Arnau
    pass