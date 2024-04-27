from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts/login')
        return render(request, 'detailedInfo.html')
