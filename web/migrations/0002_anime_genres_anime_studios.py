# Generated by Django 5.0.3 on 2024-05-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(to='web.genre'),
        ),
        migrations.AddField(
            model_name='anime',
            name='studios',
            field=models.ManyToManyField(to='web.studio'),
        ),
    ]