from django.urls import path
from .views import PatrimonioList,PatrimonioDetail,PatrimonnioCreate,PatrimonioUpdate,PatrimonioDelete




urlpatterns = [
    path('listar_patrimonio/', PatrimonioList.as_view(), name='listar_patrimonio'),
    path('detalhar_patrimonio/<int:pk>/',
         PatrimonioDetail.as_view(), name='detalhar_patrimonio'),
    path('criar_patrimonio/', PatrimonnioCreate.as_view(), name='criar_patrimonio'),
    path('atualizar_patrimonio/<int:pk>/',
         PatrimonioUpdate.as_view(), name='atualizar_patrimonio'),
path('deletar_patrimonio/<int:pk>/',
         PatrimonioDelete.as_view(), name='deletar_patrimonio'),

]