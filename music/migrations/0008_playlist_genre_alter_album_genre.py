# Generated by Django 5.0 on 2024-02-08 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_playlist_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='genre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='music.genre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='music.genre'),
            preserve_default=False,
        ),
    ]