from django import forms
from .models import MusicModel, AlbumModel

class MusicForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album'].queryset = AlbumModel.objects.filter(author=user)
        
    class Meta:
        model = MusicModel
        fields = ['title', 'file', 'album']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['name']

