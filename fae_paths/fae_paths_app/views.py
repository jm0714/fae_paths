from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Spell
from .models import Character
from django.contrib.auth.decorators import login_required

# Define a view function for the home page.
def home(request):
    # Render the 'home.html' template.
    return render(request, 'fae_paths_app/home.html')

# Define a class-based view for listing spells.
class SpellListView(ListView):
    model = Spell
    template_name = 'fae_paths_app/spell_list.html'
    context_object_name = 'spells'

@login_required(login_url="/user_auth")  # Add the login_required decorator
def character_gallery(request):
    characters = Character.objects.all()
    return render(request, 'fae_paths_app/character_gal.html', {'characters': characters})