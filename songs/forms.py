from django import forms
from . import models

class CreateSongs(forms.ModelForm):
    class Meta:
        model=models.Songs
        fields=["title","body","slug","singer","thumb"]