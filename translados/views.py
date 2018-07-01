from .models import Translado

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


class TransladoList(ListView):
    model = Translado


class TransladoDetail(DetailView):
    model = Translado



class TransladoCreate(CreateView):
    model = Translado
    fields = ['local_novo', 'sala_novo']
    success_url = '/translados/listar_translado'


