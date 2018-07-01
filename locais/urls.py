from django.urls import path
from .views import LocalList,LocalDetail,LocalCreate,LocalUpdate,LocalDelete

urlpatterns = [
    path('listar_local/', LocalList.as_view(), name='listar_local'),
    path('detalhar_local/<int:pk>/',
         LocalDetail.as_view(), name='detalhar_local'),
    path('criar_local/', LocalCreate.as_view(), name='criar_local'),
    path('atualizar_local/<int:pk>/',
         LocalUpdate.as_view(), name='atualizar_local'),
path('deletar_local/<int:pk>/',
         LocalDelete.as_view(), name='deletar_local'),

]

