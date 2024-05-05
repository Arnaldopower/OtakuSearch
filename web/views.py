from django.shortcuts import render, redirect
from django.views import View

from web.models import Anime


class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        lists = dict()
        lists['top'] = Anime.objects.top()
        lists.update(Anime.objects.by_genre())
        # lists['top2'] = Anime.objects.by_genre()
        # anime_list = Anime.objects.all()
        return render(request, 'home.html', context={'anime_list': lists})
