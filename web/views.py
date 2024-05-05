from django.shortcuts import render, redirect
from django.views import View

from web.models import Anime


class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        lists = dict()
        lists.update(Anime.objects.top())
        lists.update(Anime.objects.by_genre())
        return render(request, 'home.html', context={'anime_list': lists})


class AnimeView(View):
    def get(self, request, anime_id):
        anime = Anime.objects.get(id_anime=anime_id)
        return render(request, 'anime.html', context={'anime': anime})
