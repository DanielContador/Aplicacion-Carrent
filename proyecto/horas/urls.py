from django.urls import URLPattern, path, include
from .views import eliminarservicio, index, contacto, iniciosesion, registro, agregarservicio, modificarservicio, carrito
from .import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from rest_servicio.viewsLogin import login
urlpatterns = [
    path('', index, name="index"),
    path('contacto/', views.contacto , name='contacto'),
    path('carritos/', views.carrito , name='carrito'),
    path('index/', views.index2 , name='index2'),
    path('iniciosesion/', views.iniciosesion , name='iniciosesion'),
    path('registro/', views.registro , name='registro'),
    path('register/', views.register , name='register'),
    path('logear/', views.logear , name='logear'),
    path('logoutuser/', views.logoutuser , name='logoutuser'),
    path('agregarservicio/', views.agregarservicio , name='agregarservicio'),
    path('modificarservicio/<id>',views.modificarservicio, name='modificarservicio'),
    path('eliminarservicio/<id>', eliminarservicio, name='eliminarservicio'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
    ]



