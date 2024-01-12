from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView, TemplateView
from tienda.models import Cliente
from .models import Perfil
from .models import Servicio
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from tienda.views import clear_cart

from .forms import ServicioForm, CreateUserForm

# Create your views here.
#EJEMPLOS EN CLASES
#def index(request):
    #persona1 = Persona("Asd asd", "21", "333222")
    #lista= ["Pendulo", "Carta", "Lectura"]
    #contexto = {"nombre":"Asd Asd", "servicios" : lista, "persona":persona1}
    #return render(request, 'horas/index.html', contexto)

# metodo constructor
#class Persona:
    #def __init__(self, nombre, edad, telefono):
        #self.nombre = nombre
        #self.edad = edad
        #self.telefono = telefono
    #llama al init del padre
        #super().__init__()
 #-----------------------------------------------------------------------------------------------------       
def index(request):
    servicios = Servicio.objects.all()
    datos = {

        'servicios': servicios
    }

    return render(request, 'horas/index.html', datos)



def contacto(request):
    return render(request, 'horas/contacto.html')

def editapi(request):
    return render(request, 'frontend/lista.html')

def carrito(request):
    return render(request, 'horas/carritos.html')

def base(request):
    return render(request, 'horas/base.html')

def index2(request):
    return render(request, 'horas/index.html')

def iniciosesion(request):
    return render(request, 'horas/iniciosesion.html')

def registro(request):
    return render(request, 'horas/formu.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form=CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.save()
                cliente = Cliente(user=user)
                cliente.nombre=form.cleaned_data.get('username')
                cliente.email=form.cleaned_data.get('email')
                cliente.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Cuenta creada para: ' + user)
                return redirect('logear')
        context={'form':form}
        return render(request, 'horas/register.html', context)

def logear(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=='POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request, 'Usuario o contraseña invalido')
                

        context={}    
        return render(request,'horas/login.html',context)
    
def logoutuser(request):
    clear_cart(request) # call the clear_cart method here
    logout(request)
    return redirect('index')


def agregarservicio(request):
    datos = {
    'form':ServicioForm()
    }

    if(request.method == 'POST'):
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'


    return render(request,'horas/agregarservicio.html',datos)


def modificarservicio(request, id):
    servicio=Servicio.objects.get(id=id)


    datos= {
        'form':ServicioForm(instance=servicio)
    }


    if(request.method == 'POST'):
        formulario = ServicioForm(data=request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificado correctamente'

    return render(request, 'horas/modificarservicio.html', datos)


def eliminarservicio(request, id):
    servicio=Servicio.objects.get(id=id)
    servicio.delete()

    return redirect(to='index')

