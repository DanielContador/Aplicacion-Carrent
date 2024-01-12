from unicodedata import name
from django.urls import path
from rest_servicio.views import lista_servicio
from . import views

urlpatterns = [
    path('listar/',views.listar,name="listar"),


]

