from django.contrib.auth.models import AbstractUser
from django.db import models


# This is an example of a model in Django so that you can see how you can define your own models :D
# DON'T FORGET to run `python manage.py makemigrations` and `python manage.py migrate` after changing this file!!!


class Manga(models.Model):
    pass

class Author(models.Model):
    pass

class Status(models.Model):
    pass

class Adaptations(models.Model):
    pass

class Anime(models.Model):
    pass

class AnimeSeason(models.Model):
    id = models.IntegerField()
    animeID = models.ForeignKey(Anime, default = 1, on_delete = models.CASCADE)
    season = models.IntegerField()
    name = models.CharField(max_length=150)
    episodes = models.IntegerField()

class Genre(models.Model):
    pass

class Studio(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=150)