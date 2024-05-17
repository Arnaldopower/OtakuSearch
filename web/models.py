from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import OuterRef

from core.utils import APIHandler


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

    def get_by_id(self, anime_id):
        if not Anime.objects.filter(id=anime_id).exists():
            handler = APIHandler()
            res = handler.make_request(f'anime/{anime_id}/full')
            return self.get_anime_by_data(res['data'])
        else:
            return Anime.objects.get(id=anime_id)

    def get_anime_by_data(self, data):
        if not Status.objects.filter(name=data['status']).exists():
            status = Status(name=data['status'])
            status.save()
        else:
            status = Status.objects.get(name=data['status'])
        entry = Anime(id=data['mal_id'], name=data['titles'][0]['title'], seasons=1,
                      description=data['synopsis'],
                      cover=data['images']['jpg']['image_url'], rating=data['score'], status=status)
        if not Anime.objects.filter(id=data['mal_id']).exists():
            entry.save()
        else:
            entry = Anime.objects.get(id=data['mal_id'])
        for genre_json in data['genres']:
            if not Genre.objects.filter(genre=genre_json['name']).exists():
                genre = Genre(id=genre_json['mal_id'], genre=genre_json['name'])
                genre.save()
            else:
                genre = Genre.objects.get(genre=genre_json['name'])
            entry.genres.add(genre)
        for studio_json in data['studios']:
            if not Studio.objects.filter(name=studio_json['name']).exists():
                studio = Studio(id=studio_json['mal_id'], name=studio_json['name'])
                studio.save()
            else:
                studio = Studio.objects.get(name=studio_json['name'])
            entry.studios.add(studio)
        return entry


class Anime(models.Model):
    objects = AnimeManager()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    seasons = models.IntegerField()
    description = models.CharField(max_length=500)
    cover = models.URLField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    studios = models.ManyToManyField(Studio)

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}'


class AnimeSeason(models.Model):
    id = models.IntegerField(primary_key=True)
    animeID = models.ForeignKey(Anime, default=1, on_delete=models.CASCADE)
    season = models.IntegerField()
    name = models.CharField(max_length=150)
    episodes = models.IntegerField()


class MangaManager(models.Manager):
    def top(self):
        return {'Top': self.get_queryset().order_by('-rating')}

    def by_genre(self):
        res = {genre.genre: [manga for manga in Manga.objects.all() if genre in manga.genres.all()] for genre in
               Genre.objects.all()}
        return res

    def get_by_id(self, manga_id):
        if not Manga.objects.filter(id=manga_id).exists():
            handler = APIHandler()
            res = handler.make_request(f'manga/{manga_id}/full')
            return self.get_manga_by_data(res['data'])
        else:
            return Manga.objects.get(id=manga_id)

    def get_manga_by_data(self, data):
        if not Status.objects.filter(name=data['status']).exists():
            status = Status(name=data['status'])
            status.save()
        else:
            status = Status.objects.get(name=data['status'])
        volumes = data['volumes'] if data['volumes'] is not None else 0
        chapters = data['chapters'] if data['chapters'] is not None else 0
        description = data['synopsis'] if data['synopsis'] is not None else ""
        entry = Manga(id=data['mal_id'], name=data['titles'][0]['title'], volumes=volumes,
                      chapters=chapters, description=description,
                      cover=data['images']['jpg']['image_url'], rating=data['score'], status=status)
        if not Manga.objects.filter(id=data['mal_id']).exists():
            entry.save()
        else:
            entry = Manga.objects.get(id=data['mal_id'])
        for genre_json in data['genres']:
            if not Genre.objects.filter(genre=genre_json['name']).exists():
                genre = Genre(id=genre_json['mal_id'], genre=genre_json['name'])
                genre.save()
            else:
                genre = Genre.objects.get(genre=genre_json['name'])
            entry.genres.add(genre)
        for author_json in data['authors']:
            if not Author.objects.filter(id=author_json['mal_id']).exists():
                author = Author(id=author_json['mal_id'], name=author_json['name'])
                author.save()
            else:
                author = Author.objects.get(id=author_json['mal_id'])
            entry.authors.add(author)
        return entry


class Manga(models.Model):
    objects = MangaManager()
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


class CommentManagerAnime(models.Manager):
    def by_anime(self, anime_id):
        anime_comment = CommentAnime.objects.filter(anime_id=anime_id)
        return anime_comment


class CommentManagerManga(models.Manager):
    def by_manga(self, manga_id):
        return CommentManga.objects.filter(manga_id=manga_id)


class CommentAnime(models.Model):
    objects = CommentManagerAnime()
    id = models.IntegerField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.author}:' + '\n' + f'{self.body}'


class CommentManga(models.Model):
    objects = CommentManagerManga()
    id = models.IntegerField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.author}:' + '\n' + f'{self.body}'


class ReplyCommentAnime(models.Model):
    id = models.IntegerField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    reply = models.ForeignKey(CommentAnime, on_delete=models.CASCADE)


class RatingManager(models.Manager):
    def by_anime(self, anime_id):
        anime_rating = {anime_id: RatingFromUser.objects.filter(anime_id=anime_id)}
        return anime_rating


class RatingFromUser(models.Model):
    id = models.IntegerField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
