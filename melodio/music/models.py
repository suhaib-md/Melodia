from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='artists/', blank=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='albums/', blank=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.FileField(upload_to='songs/')
    duration = models.PositiveIntegerField()  # Duration of the song in seconds
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
