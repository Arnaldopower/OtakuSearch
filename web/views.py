from django.shortcuts import render, redirect
from django.views import View
from web.forms import CommentForm
from web.models import Anime, Comment, CommentManager
from django.core.management.base import BaseCommand

from core.utils import APIHandler
from web.models import Anime, Status, Genre, Studio


class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        lists = dict()
        lists.update(Anime.objects.top())
        lists.update(Anime.objects.by_genre())
        return render(request, 'home.html', context={'anime_list': lists})


def get_comment(anime_id):
    comments = Comment.objects.by_anime(anime_id)
    return comments


def delete_comment(comment_id):
    Comment.objects.get(id=comment_id).delete()


class AnimeView(View):
    def get(self, request, anime_id):
        try:
            anime = Anime.objects.get(id_anime=anime_id)
        except:
            handler = APIHandler()
            res = handler.make_request(f"anime/{anime_id}/full")["data"]
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
        comments = get_comment(anime_id)
        form = CommentForm()
        return render(request, 'detailedInfo.html',
                      context={'anime': anime, 'comments': comments, 'form': form, 'user': request.user})

    def post(self, request, anime_id):
        anime = Anime.objects.get(id_anime=anime_id)
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        if request.method == "POST":
            if request.POST.get('deleteComment'):
                delete_comment(request.POST.get('deleteComment'))
                form = CommentForm()
            else:
                form = CommentForm(request.POST)

                if form.is_valid():
                    Comment.objects.create(anime=anime, author=request.user, body=form.cleaned_data['body'])
        else:
            form = CommentForm()
        comments = get_comment(anime_id)
        return render(request, 'detailedInfo.html',
                      context={'anime': anime, 'comments': comments, 'form': form, 'user': request.user})


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        user = request.user
        return render(request, 'profile.html', context={'user': user})

class CommentView(View):
    def get(self, request, comment_id):
        comment = get_comment(comment_id)
        form = CommentForm()
        return render(request, 'modifyComment.html',
                      context={'form': form, 'user': request.user, 'comment': comment})

    def post(self, request, comment_id):
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                modify_comment = Comment.objects.get(id=comment_id)
                modify_comment.body = form.cleaned_data['body']
                anime_id = modify_comment.anime.id_anime
                return redirect(f'anime/{anime_id}')
        return redirect('anime/')