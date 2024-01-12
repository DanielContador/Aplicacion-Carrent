from unicodedata import name
from django.urls import path
from rest_servicio.views import lista_servicio, editarServicio
from .viewsLogin import login
from . import views

urlpatterns = [
    path('lista_servicio',lista_servicio,name="lista_servicio"),
    path('crear-servicio',views.crearServicio,name="crear-servicio"),
    path('editar-servicio/<id>/', editarServicio, name='editarServicio'),
    path('eliminar-servicio/<id>/', views.eliminarServicio, name='eliminarServicio'),
    #el del name es el que se utiliza en el html, el del medio es el que llama a la funcion de viewsLogin
    path('login',login,name='login'),

]


#path('login/<username>/<password>',login,name='login'),