from django.urls import path, include
from .views import home, SpellListView
from . import views

# Define a URL pattern for the home page.
# Define a URL pattern for a list of spells.
# Define a URL pattern for a character gallery.
# Define a URL pattern for user auth.
urlpatterns = [
    path('', home, name='home'),
    path('spell-list/', SpellListView.as_view(), name='spell_list'),
    path('character_gal/', views.character_gallery, name='character_gallery'),
    path('user_auth/', include('user_auth.urls')),

]
