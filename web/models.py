from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# This is an example of a model in Django so that you can see how you can define your own models :D
# DON'T FORGET to run `python manage.py makemigrations` and `python manage.py migrate` after changing this file!!!


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):  # Oscar
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}'


class Anime(models.Model):  # Oscar
    id_anime = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    seasons = models.IntegerField()
    description = models.CharField(max_length=500)
    cover = models.URLField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}'


class AnimeSeason(models.Model):
    id = models.IntegerField(primary_key=True)
    animeID = models.ForeignKey(Anime, default=1, on_delete=models.CASCADE)
    season = models.IntegerField()
    name = models.CharField(max_length=150)
    episodes = models.IntegerField()

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}'


class Genre(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f'ID: {self.id} Name: {self.genre}'


class Studio(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}'


class Manga(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    volumes = models.IntegerField()
    chapters = models.IntegerField()
    description = models.CharField(max_length=500)
    cover = models.URLField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}'


class Adaptations(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
