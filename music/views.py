import os
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import *


def main_page(request):
    return render(request, 'music/main_page.html')



def upload_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        file = request.FILES.get('file')
        if form.is_valid() and file.name.endswith(('.mp3', '.wav', '.flac')):
            form = form.save(commit=False)
            form.author = request.user 
            form.save()
            return redirect('main')
    else:
        form = MusicForm()
    
    return render(request, 'music/upload_music.html', {'form': form})

#def ListMusicView(ListView):
