from django.forms import ModelForm
from django import forms
from .models import Usuario


class UsuarioForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = Usuario
        fields = ['nome', 'email', 'matricula', 'senha']
