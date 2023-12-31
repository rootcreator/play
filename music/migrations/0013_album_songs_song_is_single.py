# Generated by Django 5.0 on 2023-12-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_remove_userplaylist_songs_remove_userplaylist_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='albums', to='music.song'),
        ),
        migrations.AddField(
            model_name='song',
            name='is_single',
            field=models.BooleanField(default=True),
        ),
    ]
