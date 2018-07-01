
from .models import Patrimonio
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


class PatrimonioList(ListView):
    model = Patrimonio


class PatrimonioDetail(DetailView):
    model = Patrimonio


class PatrimonnioCreate(CreateView):
    model = Patrimonio
    fields = ['tombo','nome','especificacao']
    success_url = '/patrimonios/listar_patrimonio'

class PatrimonioUpdate(UpdateView):
    model = Patrimonio
    fields = ['tombo', 'nome', 'especificacao']
    success_url = reverse_lazy('listar_patrimonio')


class PatrimonioDelete(DeleteView):
    model = Patrimonio
    success_url = reverse_lazy('listar_patrimonio')
