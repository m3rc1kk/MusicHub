from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout

def UserRegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserRegisterForm()

    return render(request, 'account/register.html', {'form' : form})



def logout_user(request):
        logout(request)
        return redirect('login')