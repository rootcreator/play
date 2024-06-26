from random import sample

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Genre(models.Model):
    GENRE_CHOICES = [
        ('Pop', 'Pop'),
        ('Hip-hop/Rap', 'Hip-hop/Rap'),
        ('R&B/Soul', 'R&B/Soul'),
        ('Rock', 'Rock'),
        ('Country', 'Country'),
        ('Electronic/Dance', 'Electronic/Dance'),
        ('Reggaeton', 'Reggaeton'),
        ('Jazz', 'Jazz'),
        ('Indie/Alternative', 'Indie/Alternative'),
        ('Latin', 'Latin'),
        ('Afrobeat', 'Afrobeat'),
        ('Highlife', 'Highlife'),
        ('Afrobeats', 'Afrobeats'),
        ('Soukous', 'Soukous'),
        ('Afro-house', 'Afro-house'),
        ('Mbalax', 'Mbalax'),
        ('Juju', 'Juju'),
        ('Rai', 'Rai'),
        ('Kizomba', 'Kizomba'),
        ('Gqom', 'Gqom'),
        ('Bollywood', 'Bollywood'),
        ('K-pop', 'K-pop'),
        ('J-pop', 'J-pop'),
        ('C-pop', 'C-pop'),
        ('Traditional_Asian', 'Traditional Asian'),
        ('Classical', 'Classical'),
        ('Folk', 'Folk'),
        ('Reggae', 'Reggae'),
        ('Metal', 'Metal'),
        ('Samba', 'Samba'),
        ('Cumbia', 'Cumbia'),
        ('Bossa_Nova', 'Bossa Nova'),
        ('Tango', 'Tango'),
        ('Andean_music', 'Andean music'),
        ('Zamba', 'Zamba'),
        ('Axé', 'Axé'),
        ('Forró', 'Forró'),
        ('Indigenous', 'Indigenous'),
    ]

    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)

    def __str__(self):
        return self.genre


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cover_image = models.ImageField(null=True, blank=True, upload_to='artist_covers/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover_image = models.ImageField(null=True, blank=True, upload_to='song_covers/')
    audio_file = models.FileField(upload_to='songs/')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True)
    feature = models.ForeignKey('Artist', related_name='featured', blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['title', 'artist']]

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='album_covers/')
    songs = models.ManyToManyField(Song, related_name='albums', blank=True)

    class Meta:
        unique_together = [['title', 'artist']]

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='playlist_covers/')
    songs = models.ManyToManyField(Song)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['title']]

    def __str__(self):
        return self.title


class GenreRadio(models.Model):
    genre_radio = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.genre} Radio"

    def create_playlist(self):
        # Get mood data for the genre
        # mood_data = Mood.objects.filter(genre=self.genre)

        # Get trend data for the genre
        # trend_data = Trends.objects.filter(genre=self.genre)

        # Dummy logic to select songs based on mood and trends
        selected_songs = Song.objects.filter(genre=self.genre)

        # Define different themes or variations for playlists
        themes = ['Party', 'Relaxing', 'Workout', 'Chill', 'Study']

        for theme in themes:
            # Shuffle the selected songs to mix them up
            shuffled_songs = sample(list(selected_songs), min(len(selected_songs), 24))  # Select up to 24 songs

            # Create playlist title based on theme, mood, and trends
            playlist_title = f"{self.genre} Radio Playlist - {theme}"

            # Check if playlist with the same title already exists
            existing_playlist = Playlist.objects.filter(title=playlist_title).exists()

            if not existing_playlist:
                # Create the playlist only if it doesn't already exist
                playlist = Playlist.objects.create(title=playlist_title, genre=self.genre)
                playlist.songs.add(*shuffled_songs)

    @receiver(post_save, sender=Genre)
    def create_or_update_genreradio(sender, instance, **kwargs):
        for genre in Genre.objects.all():
            genreradio, created = GenreRadio.objects.get_or_create(genre=genre)
            genreradio.create_playlist()


class ArtistRadio(models.Model):
    artist_radio = models.ForeignKey(Artist, on_delete=models.CASCADE)

    # mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} Radio"

    def create_playlist(self):
        # Get songs by the associated artist
        songs_by_artist = Song.objects.filter(artist=self.artist)

        # Define different themes or variations for playlists
        themes = ['Top Hits', 'Old Favorites', 'Acoustic Sessions', 'Collaborations' 'Live Performances']

        for theme in themes:
            # Shuffle the songs to mix them up
            shuffled_songs = sample(list(songs_by_artist), min(len(songs_by_artist), 10))  # Select up to 10 songs

            # Create playlist title based on theme and artist
            playlist_title = f"{self.artist} Radio Playlist - {theme}"

            # Check if playlist with the same title already exists
            existing_playlist = Playlist.objects.filter(title=playlist_title).exists()

            if not existing_playlist:
                # Create the playlist only if it doesn't already exist
                playlist = Playlist.objects.create(title=playlist_title, artist=self.artist)
                playlist.songs.add(*shuffled_songs)


'''
class MusicAPI:
    BASE_URL = 'http://localhost:8000/api/'  # Replace with your Django app's base URL

    @staticmethod
    def fetch_data(endpoint):
        url = MusicAPI.BASE_URL + endpoint
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch {endpoint}. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None

    @staticmethod
    def fetch_genres():
        return MusicAPI.fetch_data('genres/')

    @staticmethod
    def fetch_artists():
        return MusicAPI.fetch_data('artists/')

    @staticmethod
    def fetch_composers():
        return MusicAPI.fetch_data('composers/')

    @staticmethod
    def fetch_albums():
        return MusicAPI.fetch_data('albums/')

    @staticmethod
    def fetch_songs():
        return MusicAPI.fetch_data('songs/')
'''
