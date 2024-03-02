# Generated by Django 5.0.2 on 2024-02-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='feature',
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='album',
            name='mood',
        ),
        migrations.RemoveField(
            model_name='song',
            name='mood',
        ),
        migrations.RemoveField(
            model_name='album',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='song',
            name='composer',
        ),
        migrations.RemoveField(
            model_name='song',
            name='is_single',
        ),
        migrations.RemoveField(
            model_name='song',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='song',
            name='rating',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Mood',
        ),
    ]
