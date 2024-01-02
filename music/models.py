from django.db import models
from django.contrib.auth.models import User

class AlbumModel(models.Model):
    name = models.CharField(max_length = 25)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.name



class MusicModel(models.Model):
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to='music_file/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(null = True, auto_now_add = True)
    album = models.ForeignKey(AlbumModel, on_delete = models.CASCADE, null = True, blank = True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title