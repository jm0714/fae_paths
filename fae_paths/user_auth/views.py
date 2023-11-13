from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# View for rendering the login page
def user_login(request):
    return render(request, 'authentication/login.html')

# View for authenticating a user
def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('user_auth:login'))
        else:
            return redirect('user_auth:login')
            
# View for displaying user information    
def show_user(request):
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password 
    })

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)