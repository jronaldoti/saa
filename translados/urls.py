from django.urls import path
from .views import TransladoList,TransladoDetail,TransladoCreate



urlpatterns = [
    path('listar_translado/', TransladoList.as_view(), name='listar_translado'),
    path('detalhar_translado/<int:pk>/',
         TransladoDetail.as_view(), name='detalhar_translado'),
    path('criar_translado/', TransladoCreate.as_view(), name='criar_translado'),
]
