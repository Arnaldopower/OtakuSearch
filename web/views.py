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


def edit_comment(comment_id, new_body):
    comment = Comment.objects.get(id=comment_id)
    comment.body = new_body
    comment.save()


class AnimeView(View):
    def get(self, request, anime_id):
        anime = Anime.objects.get(id_anime=anime_id)
        comments = get_comment(anime_id)
        form = CommentForm()
        form_edit_comment = CommentForm()
        return render(request, 'detailedInfo.html',
                      context={'anime': anime, 'comments': comments, 'form': form, 'user': request.user,
                               'form_edit_comment': form_edit_comment})

    def post(self, request, anime_id):
        anime = Anime.objects.get(id_anime=anime_id)

        comments = get_comment(anime_id)
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        if request.method == "POST":
            if request.POST.get('deleteComment'):
                delete_comment(request.POST.get('deleteComment'))
            elif request.POST.get('modifyComment'):
                form_edit_comment = CommentForm(request.POST)
                if form_edit_comment.is_valid():
                    edit_comment(request.POST.get('modifyComment'), form_edit_comment.cleaned_data['body'])
            else:
                form = CommentForm(request.POST)
                if form.is_valid():
                    Comment.objects.create(anime=anime, author=request.user, body=form.cleaned_data['body'])
        form_edit_comment = CommentForm()
        form = CommentForm()
        return render(request, 'detailedInfo.html',
                      context={'anime': anime, 'comments': comments, 'form': form, 'user': request.user,
                               'form_edit_comment': form_edit_comment})


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        user = request.user
        return render(request, 'profile.html', context={'user': user})
