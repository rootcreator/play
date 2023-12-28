# Generated by Django 5.0 on 2023-12-27 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_album_rating_song_rating'),
        ('users', '0005_alter_userlibrary_created_playlists_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlibrary',
            name='created_playlists',
            field=models.ManyToManyField(blank=True, related_name='created_in_libraries', to='music.playlist'),
        ),
        migrations.AlterField(
            model_name='userlibrary',
            name='favorite_artists',
            field=models.ManyToManyField(blank=True, related_name='favorited_in_libraries', to='music.artist'),
        ),
        migrations.AlterField(
            model_name='userlibrary',
            name='saved_albums',
            field=models.ManyToManyField(blank=True, related_name='saved_in_libraries', to='music.album'),
        ),
        migrations.AlterField(
            model_name='userlibrary',
            name='saved_songs',
            field=models.ManyToManyField(blank=True, related_name='saved_in_libraries', to='music.song'),
        ),
        migrations.AlterField(
            model_name='userlibrary',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='library', to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofileview',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_views', to='users.userprofile'),
        ),
    ]
