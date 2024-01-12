from django.urls import path
from . import views


urlpatterns = [
    path('tienda/', views.tienda, name="tienda"),
    path('orden/', views.orden, name="orden"),
    path('eliminar/<id>', views.eliminar, name="eliminar"),
    path('editar/', views.editar, name="editar"),
    path('maintienda/', views.maintienda, name="maintienda"),
    path('carrito/', views.carrito, name="carrito"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('todos/', views.todos, name='todos'),
    path('cambiar/<id>', views.cambiar_producto, name='cambiar'),
    path('pago_exitoso/', views.pago_exitoso, name='pago_exitoso'),
]   
