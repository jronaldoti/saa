from .models import Local
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class LocalList(ListView):
    model = Local


class LocalDetail(DetailView):
    model = Local



class LocalCreate(CreateView):
    model = Local
    fields = ['nome', 'rua', 'numero', 'bairro']
    success_url = '/locais/listar_local'


class LocalUpdate(UpdateView):
    model = Local
    fields = ['nome', 'rua', 'numero', 'bairro']
    success_url = reverse_lazy('listar_local')

class LocalDelete(DeleteView):
    model = Local
    success_url = reverse_lazy('listar_local')


