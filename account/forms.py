from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name', 'password1', 'password2', 'email']


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        
        if any(char.isdigit() for char in first_name):
            raise ValidationError('Имя содержит цифры')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        
        if any(char.isdigit() for char in last_name):
            raise ValidationError('Фамилия содержит цифры')
        return last_name
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise ValidationError('Такой пользователь уже существует')
        return username

    

class LoginForm(AuthenticationForm):
    pass

    

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']
        if not authenticate(username = username, password = password):
            raise ValidationError('Пароль не подходит')
        return password