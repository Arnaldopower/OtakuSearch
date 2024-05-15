from django.contrib import admin

# This is how you can register your models with the Django admin so that you can manage them from the admin interface

from .models import Manga, Author, Status, Adaptations, Anime, AnimeSeason, Genre, Studio, Comment, RatingFromUser

admin.site.register(Manga)
admin.site.register(Author)
admin.site.register(Status)
admin.site.register(Adaptations)
admin.site.register(Anime)
admin.site.register(AnimeSeason)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Comment)
admin.site.register(RatingFromUser)
