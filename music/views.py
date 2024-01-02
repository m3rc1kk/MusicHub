import os
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView
from .forms import *
from .permissions import *
from django.contrib.auth.mixins import LoginRequiredMixin

def main_page(request):
    return render(request, 'music/main_page.html')



def upload_music(request):
    if request.method == 'POST':
        form = MusicForm(request.user, request.POST, request.FILES)
        file = request.FILES.get('file')
        if form.is_valid() and file.name.endswith(('.mp3', '.wav', '.flac')):
            form = form.save(commit=False)
            form.author = request.user 
            form.save()
            return redirect('home')
    else:
        form = MusicForm(request.user)
    
    return render(request, 'music/upload_music.html', {'form': form})

class ListMusicView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = MusicModel
    template_name = 'music/home_page.html'

   

class DeleteMusicView(AuthorPermissionsMixin,DeleteView):
    model = MusicModel
    success_url = reverse_lazy('home')



def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('album-list')
    else:
        form = AlbumForm()
        
    return render(request, 'music/create_album.html', {'form': form})


class AlbumMusicView(ListView):
    paginate_by = 4
    model = AlbumModel
    template_name = 'music/album_page.html'

def AlbumDetailView(request, pk):
    albums = AlbumModel.objects.filter(id = pk)
    music = MusicModel.objects.all()

    return render(request, 'music/album_detail.html', {'music': music, 'albums': albums})


class DeleteAlbumView(AuthorPermissionsMixin,DeleteView):
    model = AlbumModel
    success_url = reverse_lazy('home')