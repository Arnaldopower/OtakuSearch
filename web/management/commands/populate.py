from django.core.management.base import BaseCommand

from core.utils import APIHandler
from web.models import Anime, Status, Genre, Studio, Manga, Author


class Command(BaseCommand):
    help = 'Populate DB using external API'

    def handle(self, *args, **options):
        handler = APIHandler()
        for req_type in ['anime', 'manga']:
            print(f'Fetching {req_type} info...')
            for page in range(1, 5):
                print(f'Fetching page {page}...', end='\r')
                top_res = handler.make_request(f'top/{req_type}?page={page}')
                if not top_res:
                    continue
                top_res = top_res['data']
                for res in top_res:
                    if not Status.objects.filter(name=res['status']).exists():
                        status = Status(name=res['status'])
                        status.save()
                    else:
                        status = Status.objects.get(name=res['status'])
                    entry = None
                    if req_type == 'anime':
                        entry = Anime(id=res['mal_id'], name=res['titles'][0]['title'], seasons=1,
                                      description=res['synopsis'],
                                      cover=res['images']['jpg']['image_url'], rating=res['score'], status=status)
                        if not Anime.objects.filter(id=res['mal_id']).exists():
                            entry.save()
                        else:
                            entry = Anime.objects.get(id=res['mal_id'])
                    else:
                        volumes = res['volumes'] if res['volumes'] is not None else 0
                        chapters = res['chapters'] if res['chapters'] is not None else 0
                        entry = Manga(id=res['mal_id'], name=res['titles'][0]['title'], volumes=volumes,
                                      chapters=chapters, description=res['synopsis'],
                                      cover=res['images']['jpg']['image_url'], rating=res['score'], status=status)
                        if not Manga.objects.filter(id=res['mal_id']).exists():
                            entry.save()
                        else:
                            entry = Manga.objects.get(id=res['mal_id'])
                    for genre_json in res['genres']:
                        if not Genre.objects.filter(genre=genre_json['name']).exists():
                            genre = Genre(id=genre_json['mal_id'], genre=genre_json['name'])
                            genre.save()
                        else:
                            genre = Genre.objects.get(genre=genre_json['name'])
                        entry.genres.add(genre)
                    if req_type == 'anime':
                        for studio_json in res['studios']:
                            if not Studio.objects.filter(name=studio_json['name']).exists():
                                studio = Studio(id=studio_json['mal_id'], name=studio_json['name'])
                                studio.save()
                            else:
                                studio = Studio.objects.get(name=studio_json['name'])
                            entry.studios.add(studio)
                    else:
                        for author_json in res['authors']:
                            if not Author.objects.filter(id=author_json['mal_id']).exists():
                                author = Author(id=author_json['mal_id'], name=author_json['name'])
                                author.save()
                            else:
                                author = Author.objects.get(id=author_json['mal_id'])
                            entry.authors.add(author)
