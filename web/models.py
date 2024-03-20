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
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)


class Anime(models.Model):
    pass


class AnimeSeason(models.Model):
    id = models.IntegerField()
    animeID = models.ForeignKey(Anime, default = 1, on_delete = models.CASCADE)
    season = models.IntegerField()
    name = models.CharField(max_length=150)
    episodes = models.IntegerField()


class Genre(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    genero = models.CharField(max_length=50)


class Studio(models.Model):
  id = models.IntegerField()
  name = models.CharField(max_length=150)

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
