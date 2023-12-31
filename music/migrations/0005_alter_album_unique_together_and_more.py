# Generated by Django 5.0 on 2024-01-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_album_genre'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='album',
            unique_together={('title', 'artist', 'cover_image')},
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together={('title',)},
        ),
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('title', 'artist')},
        ),
        migrations.AddConstraint(
            model_name='userlibrary',
            constraint=models.UniqueConstraint(fields=('user_profile',), name='unique_user_library'),
        ),
    ]
