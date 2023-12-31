# Generated by Django 5.0 on 2023-12-26 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_remove_playlist_songs_remove_playlist_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='cover_image',
            field=models.ImageField(default=1, upload_to='album_covers/'),
            preserve_default=False,
        ),
    ]
