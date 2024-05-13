from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views import View

from web.forms import LoginForm, SignUpForm


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('home')


class SignUpView(View):
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'registration/account.html', {"form": form, "sign_up": True})

    def get(self, request):
        if not request.user.is_authenticated:
            form = SignUpForm()
            return render(request, 'registration/account.html', {"form": form, "sign_up": True})
        return redirect('home')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/account.html', {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'registration/account.html', {"form": form})

class DeleteView(View):
    def get(self, request):
        pass
    
    def post(self, request):
        user = request.user
        user.delete()
        return redirect('login')