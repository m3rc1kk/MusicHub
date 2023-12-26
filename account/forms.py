from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']


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