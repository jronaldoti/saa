from .models import Sala
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy



class SalaList(ListView):
    model = Sala


class SalaDetail(DetailView):
    model = Sala



class SalaCreate(CreateView):
    model = Sala
    fields = ['local', 'nome', 'numero']
    success_url = '/salas/listar_sala'


class SalaUpdate(UpdateView):
    model = Sala
    fields = ['local', 'nome', 'numero']
    success_url = reverse_lazy('listar_sala')

class SalaDelete(DeleteView):
    model = Sala
    success_url = reverse_lazy('listar_sala')