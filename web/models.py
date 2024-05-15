from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import OuterRef


# This is an example of a model in Django so that you can see how you can define your own models :D
# DON'T FORGET to run `python manage.py makemigrations` and `python manage.py migrate` after changing this file!!!


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(max_length=50)

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


class AnimeManager(models.Manager):
    def top(self):
        return {'Top': self.get_queryset().order_by('-rating')}

    def by_genre(self):
        res = {genre.genre: [anime for anime in Anime.objects.all() if genre in anime.genres.all()] for genre in
               Genre.objects.all()}
        return res


class Anime(models.Model):
    objects = AnimeManager()
    id_anime = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    seasons = models.IntegerField()
    description = models.CharField(max_length=500)
    cover = models.URLField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    studios = models.ManyToManyField(Studio)

    def __str__(self):
        return f'ID: {self.id_anime} Name: {self.name}'


class AnimeSeason(models.Model):
    id = models.IntegerField(primary_key=True)
    animeID = models.ForeignKey(Anime, default=1, on_delete=models.CASCADE)
    season = models.IntegerField()
    name = models.CharField(max_length=150)
    episodes = models.IntegerField()


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


class CommentManager(models.Manager):
    def by_anime(self, anime_id):
        anime_comment = Comment.objects.filter(anime_id=anime_id)
        return anime_comment


class Comment(models.Model):
    objects = CommentManager()
    id = models.IntegerField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.author}:' + '\n' + f'{self.body}'


class ReplyComment(models.Model):
    id = models.IntegerField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    reply = models.ForeignKey(Comment, on_delete=models.CASCADE)


class RatingManager(models.Manager):
    def by_anime(self, anime_id):
        anime_rating = {anime_id: RatingFromUser.objects.filter(anime_id=anime_id)}
        return anime_rating


class RatingFromUser(models.Model):
    id = models.IntegerField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
