
from django.urls import path
from .views import index, crear_clientes_predeterminados, prueba_busqueda, crear_cliente 

app_name='cliente'

urlpatterns = [
    path('', index, name='index'),
    path('crear-clientes/',crear_clientes_predeterminados ,name='crear-clientes'),
    path('prueba-busqueda/', prueba_busqueda, name='prueba-busqueda'),
    path('crear/',crear_cliente,name='crear')
]


