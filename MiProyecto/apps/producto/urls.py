from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index' ),
    path('producto_categoria_list/', views.ProductoCategoriaList.as_view(), name= "producto_categoria_list"),
    path('producto_categoria_pedido/', views.producto_categoria_pedido, name='producto_categoria_pedido'),
    path('producto_categoria_delete/<int:id>', views.producto_categoria_delete, name='producto_categoria_delete'),
    path('producto_categoria_update/<int:id>', views.producto_categoria_update, name='producto_categoria_update'),
]
    