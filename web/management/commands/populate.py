from django.core.management.base import BaseCommand

from core.utils import APIHandler
from web.models import Anime, Status, Genre, Studio


class Command(BaseCommand):
    help = 'Populate DB using external API'

    def handle(self, *args, **options):
        handler = APIHandler()
        for page in range(1, 10):
            top_res = handler.make_request(f'seasons/now?page={page}')['data']
            for res in top_res:
                if not Status.objects.filter(name=res['status']).exists():
                    status = Status(name=res['status'])
                    status.save()
                else:
                    status = Status.objects.get(name=res['status'])
                anime = Anime(id_anime=res['mal_id'], name=res['titles'][0]['title'], seasons=1,
                              description=res['synopsis'],
                              cover=res['images']['jpg']['image_url'], rating=res['score'], status=status)
                if not Anime.objects.filter(id_anime=res['mal_id']).exists():
                    anime.save()
                else:
                    anime = Anime.objects.get(id_anime=res['mal_id'])
                for genre_json in res['genres']:
                    if not Genre.objects.filter(genre=genre_json['name']).exists():
                        genre = Genre(id=genre_json['mal_id'], genre=genre_json['name'])
                        genre.save()
                    else:
                        genre = Genre.objects.get(genre=genre_json['name'])
                    anime.genres.add(genre)
                for studio_json in res['studios']:
                    if not Studio.objects.filter(name=studio_json['name']).exists():
                        studio = Studio(id=studio_json['mal_id'], name=studio_json['name'])
                        studio.save()
                    else:
                        studio = Studio.objects.get(name=studio_json['name'])
                    anime.studios.add(studio)
