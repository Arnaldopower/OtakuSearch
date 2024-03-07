from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

from web.forms import NameForm


class MemberView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'members.html')
        return redirect('home')


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('members')
        else:
            form = NameForm()
            return render(request, 'home.html', {"form": form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('members')
        return render(request, 'home.html')


class GetNameView(View):
    def get(self, request):
        form = NameForm()
        return render(request, "name.html", {"form": form})
