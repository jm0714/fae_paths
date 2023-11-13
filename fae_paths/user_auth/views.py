from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def user_login(request):
    """
    Render the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered login page.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Authenticate a user based on the provided credentials.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page upon successful authentication,
                             otherwise redirects back to the login page.
    """
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('user_auth:login'))
        else:
            return redirect('user_auth:login')

def show_user(request):
    """
    Display user information.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered user information page.
    """
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password 
    })

def register(request):
    """
    Handle user registration.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered registration page or redirects to the login page upon successful registration.
    """
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
