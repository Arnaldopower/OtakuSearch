"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include

from web.views import HomeView, EntryView, ProfileView, CommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),  # Create a new path for the home page
    path("accounts/", include("accounts.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("entry/<str:entry_type>/<int:entry_id>/", EntryView.as_view(), name="entry"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("manga/",  HomeView.as_view(), name="home_manga"),
    path("anime/",  HomeView.as_view(), name="home_anime"),


]
