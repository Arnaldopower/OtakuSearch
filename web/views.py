from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from web.forms import CommentForm
from web.models import Anime, Manga, CommentAnime, CommentManga
from web.models import Anime, Status, Genre, Studio
from core.utils import APIHandler


class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        req_type = request.GET.get('type', 'anime')
        req_type = 'anime' if req_type not in ['anime', 'manga'] else req_type
        entry_list = dict()
        if req_type == 'anime':
            entry_list.update(Anime.objects.top())
            entry_list.update(Anime.objects.by_genre())
        else:
            entry_list.update(Manga.objects.top())
            entry_list.update(Manga.objects.by_genre())
        return render(request, 'home.html', context={'entry_list': entry_list, 'type': req_type})

class SearchView(View):
    def get(self, request, anime_id):
        anime = Anime.objects.get(id_anime=anime_id)
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



def get_comment(entry_id, entry_type):
    if entry_type == 'anime':
        return CommentAnime.objects.by_anime(entry_id)
    else:
        return CommentManga.objects.by_manga(entry_id)


def delete_comment(comment_id, entry_type):
    if entry_type == 'anime':
        CommentAnime.objects.get(id=comment_id).delete()
    else:
        CommentManga.objects.get(id=comment_id).delete()


def edit_comment(comment_id, new_body, entry_type):
    if entry_type == 'anime':
        comment_anime = CommentAnime.objects.get(id=comment_id)
        comment_anime.body = new_body
        comment_anime.save()
    else:
        comment_manga = CommentManga.objects.get(id=comment_id)
        comment_manga.body = new_body
        comment_manga.save()


@method_decorator(login_required, name='dispatch')
class EntryView(View):
    def get(self, request, entry_type, entry_id):
        entry = None
        if entry_type == 'anime':
            entry = Anime.objects.get_by_id(entry_id)
        else:
            entry = Manga.objects.get_by_id(entry_id)
        comments = get_comment(entry_id, entry_type)
        form = CommentForm()
        print(entry_type)
        print(request.user)
        return render(request, 'detailedInfo.html',
                      context={'anime': entry, 'comments': comments, 'form': form, 'user': request.user})

    def post(self, request, entry_type, entry_id):
        if entry_type == 'anime':
            entry = Anime.objects.get(id=entry_id)
        else:
            entry = Manga.objects.get(id=entry_id)
        if request.method == "POST":
            if request.POST.get('deleteComment'):
                delete_comment(request.POST.get('deleteComment'), entry_type)
            elif request.POST.get('modifyComment'):
                form_edit_comment = CommentForm(request.POST)
                if form_edit_comment.is_valid():
                    edit_comment(request.POST.get('modifyComment'), form_edit_comment.cleaned_data['body'], entry_type)
            else:
                form = CommentForm(request.POST)
                if form.is_valid():
                    if entry_type == 'anime':
                        CommentAnime.objects.create(anime=entry, author=request.user, body=form.cleaned_data['body'])
                    else:
                        CommentManga.objects.create(manga=entry, author=request.user, body=form.cleaned_data['body'])

        comments = get_comment(entry_id, entry_type)
        form_edit_comment = CommentForm()
        form = CommentForm()
        return render(request, 'detailedInfo.html',
                      context={'entry': entry, 'entry_type': entry_type, 'comments': comments, 'form': form,
                               'user': request.user,
                               'form_edit_comment': form_edit_comment})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        user = request.user
        return render(request, 'profile.html', context={'user': user})


@method_decorator(login_required, name='dispatch')
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
                modify_comment = CommentAnime.objects.get(id=comment_id)
                modify_comment.body = form.cleaned_data['body']
                anime_id = modify_comment.anime.id_anime
                return redirect(f'anime/{anime_id}')
        return redirect('anime/')
