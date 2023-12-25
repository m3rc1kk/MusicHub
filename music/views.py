import os
from django.http import FileResponse
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
            return redirect('home')
    else:
        form = MusicForm()
    
    return render(request, 'music/upload_music.html', {'form': form})

class ListMusicView(ListView):
    paginate_by = 4
    model = MusicModel
    template_name = 'music/home_page.html'


