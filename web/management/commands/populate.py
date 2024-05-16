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
                    if req_type == 'anime':
                        Anime.objects.get_anime_by_data(res)
                    else:
                        Manga.objects.get_manga_by_data(res)
