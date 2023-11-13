from django.db import models

# Create your models here.
class Meta:
    app_label = 'fae_paths'

# Define a model for representing Spells.
class Spell(models.Model):
    # Field to store the name of the spell (limited to 100 characters).
    name = models.CharField(max_length=100)

    # Field to store the description of the spell (text field for longer descriptions).
    description = models.TextField()

    # A human-readable representation of a Spell object.
    def __str__(self):
        return self.name

# Define a model for representing Characters.
class Character(models.Model):
    # Field to store the name of the character (limited to 100 characters).
    name = models.CharField(max_length=100)

    # Field to store the image path of the character (limited to 255 characters).
    image_path = models.CharField(max_length=255)

    # A human-readable representation of a Character object.
    def __str__(self):
        return self.name