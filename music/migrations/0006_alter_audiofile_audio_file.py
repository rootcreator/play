# Generated by Django 5.0 on 2024-01-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_album_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audio_file',
            field=models.FileField(upload_to='songs/'),
        ),
    ]
