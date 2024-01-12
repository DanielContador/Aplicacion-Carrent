from django import forms
from django.forms import ModelForm
from .models import Servicio
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['precio', 'nombreServicio', 'descripcion']


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
                                                              
                               