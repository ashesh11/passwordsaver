from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import PasswordSaver

class PasswordSaverForm(ModelForm):
    class Meta:
        model = PasswordSaver
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']