from msilib.schema import ListView
from re import template
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .forms import PasswordSaverForm, CreateUserForm
from .models import PasswordSaver

@login_required(login_url='login-page')
def add_password(request):
    form = PasswordSaverForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = PasswordSaverForm()
            messages.success(request, 'Password Added Sucessfully')
    return render(request, 'main/add_password.html', {'form': form})

@login_required(login_url='login-page')
def see_password(request):
    user = PasswordSaver.objects.all()
    return render(request, 'main/see_password.html', {'user': user})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('add-password')

    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('login-page')

def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for '+ user)
            return redirect('login-page')
    return render(request, 'main/register.html', {'form':form})