from django.urls import path
from .views import SalaList,SalaDetail,SalaCreate,SalaUpdate,SalaDelete



urlpatterns = [
    path('listar_sala/', SalaList.as_view(), name='listar_sala'),
    path('detalhar_sala/<int:pk>/',
         SalaDetail.as_view(), name='detalhar_sala'),
    path('criar_sala/', SalaCreate.as_view(), name='criar_sala'),
    path('atualizar_sala/<int:pk>/',
         SalaUpdate.as_view(), name='atualizar_sala'),
path('deletar_sala/<int:pk>/',
         SalaDelete.as_view(), name='deletar_sala'),

]