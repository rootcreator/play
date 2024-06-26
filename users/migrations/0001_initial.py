# Generated by Django 5.0.2 on 2024-03-18 12:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('music', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_playlists', models.ManyToManyField(blank=True, related_name='created_in_library', to='music.playlist')),
                ('favorite_artists', models.ManyToManyField(blank=True, related_name='favorite_in_library', to='music.artist')),
                ('saved_albums', models.ManyToManyField(blank=True, related_name='saved_in_library', to='music.album')),
                ('saved_playlists', models.ManyToManyField(blank=True, related_name='saved_in_library', to='music.playlist')),
                ('saved_songs', models.ManyToManyField(blank=True, related_name='saved_in_library', to='music.song')),
            ],
            options={
                'db_table': 'profile_user_library',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListeningHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listened_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song')),
                ('user_library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.library')),
            ],
            options={
                'db_table': 'profile_listening_history',
            },
        ),
        migrations.AddField(
            model_name='library',
            name='recently_played',
            field=models.ManyToManyField(blank=True, related_name='played_by_users', through='users.ListeningHistory', to='music.song'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('bio', models.TextField(blank=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('last_viewed', models.DateTimeField(auto_now=True)),
                ('favourite_genres', models.ManyToManyField(to='music.genre')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='listeninghistory',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='library',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='library', to='users.profile'),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], default='light', help_text='Choose app theme', max_length=20)),
                ('notifications_enabled', models.BooleanField(default=True, help_text='Enable notifications')),
                ('auto_play_enabled', models.BooleanField(default=False, help_text='Enable auto-play feature')),
                ('repeat_mode', models.CharField(choices=[('none', 'None'), ('all', 'All'), ('one', 'One')], default='none', help_text='Set repeat mode', max_length=20)),
                ('language', models.CharField(default='en', help_text='Choose app language', max_length=20)),
                ('download_quality', models.CharField(choices=[('standard', 'Standard'), ('high', 'High'), ('lossless', 'Lossless')], default='standard', help_text='Set download quality', max_length=20)),
                ('streaming_quality', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', help_text='Set streaming quality', max_length=20)),
                ('equalizer_enabled', models.BooleanField(default=False, help_text='Enable equalizer')),
                ('local_files_access', models.BooleanField(default=False, help_text='Enable access to local files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
