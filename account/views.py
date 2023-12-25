from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.contrib.auth import login, logout
from music.models import MusicModel
from django.core.paginator import Paginator

def UserRegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'account/register.html', {'form' : form})



def logout_user(request):
        logout(request)
        return redirect('login')


class DetailUser(generic.DetailView):

    model = User
    template_name = 'account/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musicmodel'] = MusicModel.objects.all()
        return context
