
from .models import Usuario
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


class UsuarioList(ListView):
    model = Usuario


class UsuarioDetail(DetailView):
    model = Usuario


class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['nome','email','matricula','senha']
    success_url = '/usuarios/listar_user'

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['nome', 'email', 'matricula', 'senha']
    success_url = reverse_lazy('listar_usuario')


class UsuarioDelete(DeleteView):
    model = Usuario
    success_url = reverse_lazy('listar_usuario')
