from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


class MemberView(View):
    def get(self, request):
        return render(request, 'members.html')


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('members')
        else:
            return render(request, 'home.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('members')
        return render(request, 'home.html')
