from django.contrib import admin
from django.urls import path, include
from usuarios import urls as usuarios_urls
from locais import urls as locais_urls
from patrimonios import urls as patrimonios_urls
from salas import urls as salas_urls
from translados import urls as translados_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(usuarios_urls)),
    path('locais/', include(locais_urls)),
    path('patrimonios/',include(patrimonios_urls)),
    path('salas/',include(salas_urls)),
    path('translados/',include(translados_urls)),

]
