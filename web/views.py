from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from web.forms import CommentForm
from web.models import Anime, Comment, CommentManager


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
        anime = Anime.objects.get(id_anime=anime_id)
        comments = get_comment(anime_id)
        form = CommentForm()
        return render(request, 'anime.html',
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
        return render(request, 'anime.html',
                      context={'anime': anime, 'comments': comments, 'form': form, 'user': request.user})


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
