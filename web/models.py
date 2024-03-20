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
    pass

class Genre(models.Model):
    pass

class Studio(models.Model):
    pass