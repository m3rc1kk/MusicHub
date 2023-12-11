from django import forms
from .models import MusicModel

class MusicForm(forms.ModelForm):
    class Meta:
        model = MusicModel
        fields = ['title', 'file']