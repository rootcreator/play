# Generated by Django 5.0.2 on 2024-02-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_song_ft_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='ft_artist',
            field=models.CharField(max_length=100),
        ),
    ]
