# Generated by Django 5.0.2 on 2024-03-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_song_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='mood',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='mood',
        ),
        migrations.RemoveField(
            model_name='song',
            name='mood',
        ),
    ]
