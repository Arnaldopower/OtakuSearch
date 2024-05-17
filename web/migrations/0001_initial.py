# Generated by Django 5.0.6 on 2024-05-17 07:21

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('seasons', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('cover', models.URLField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AnimeSeason',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('season', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('episodes', models.IntegerField()),
                ('animeID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.anime')),
            ],
        ),
        migrations.CreateModel(
            name='CommentAnime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.anime')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(to='web.genre'),
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('volumes', models.IntegerField()),
                ('chapters', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('cover', models.URLField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('authors', models.ManyToManyField(to='web.author')),
                ('genres', models.ManyToManyField(to='web.genre')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.status')),
            ],
        ),
        migrations.CreateModel(
            name='CommentManga',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.manga')),
            ],
        ),
        migrations.CreateModel(
            name='Adaptations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.anime')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.manga')),
            ],
        ),
        migrations.CreateModel(
            name='RatingFromUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyCommentAnime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.anime')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.commentanime')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.status'),
        ),
        migrations.AddField(
            model_name='anime',
            name='studios',
            field=models.ManyToManyField(to='web.studio'),
        ),
    ]
