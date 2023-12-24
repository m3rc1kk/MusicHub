from django.db import models
from django.contrib.auth.models import User

class MusicModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='music_file/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(null = True, auto_now_add = True)
    
    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title