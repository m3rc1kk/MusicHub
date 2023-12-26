import os
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .forms import *
from .permissions import *
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ListMusicView(LoginRequiredMixin, ListView):
    paginate_by = 4
    model = MusicModel
    template_name = 'music/home_page.html'


class DeleteMusicView(AuthorPermissionsMixin,DeleteView):
    model = MusicModel
    success_url = reverse_lazy('home')
