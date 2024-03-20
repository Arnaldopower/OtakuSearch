from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# This is an example of a model in Django so that you can see how you can define your own models :D
# DON'T FORGET to run `python manage.py makemigrations` and `python manage.py migrate` after changing this file!!!
class Content(models.Model):
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


class Manga(models.Model):
    manga_id = models.IntegerField(primary_key=True)
    name = models.CharField(150)
    volumes = models.IntegerField()
    chapters = models.IntegerField()
    description = models.CharField(500)
    cover = models.URLField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    status = models.ForeignKey(Status, on_delete=models.SET_NULL)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}'
