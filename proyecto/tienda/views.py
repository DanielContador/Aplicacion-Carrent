from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.decorators import login_required
from .forms import addCarForm
from .models import Orden, OrdenProducto, Producto

# Create your views here.
@login_required(login_url='logear')
def tienda(request):
    
    if request.user.is_authenticated:
        cliente= request.user.cliente
        user_groups = list(request.user.groups.all().values_list('name', flat=True))
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_cart_items
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = orden['get_cart_items']
        
    productos = Producto.objects.filter(disponible=True)
    context={'productos':productos, 'cartItems':cartItems, 'user_groups': user_groups}
    return render(request, 'tienda/tienda.html', context)

@login_required(login_url='logear')
def orden(request):
    

        
    orden = Orden.objects.all()
    ordenproducto = OrdenProducto.objects.all()
    context={'orden':orden,'ordenproducto':ordenproducto}
    return render(request, 'tienda/orden.html', context)


# @login_required(login_url='logear')
# def todos(request):
    
#     if request.user.is_authenticated:
#         cliente= request.user.cliente
#         user_groups = list(request.user.groups.all().values_list('name', flat=True))
#         orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
#         items = orden.ordenproducto_set.all()
#         cartItems = orden.get_cart_items
#     else:
#         items = []
#         orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
#         cartItems = orden['get_cart_items']
        
#     productos = Producto.objects.all
#     context={'productos':productos, 'cartItems':cartItems, 'user_groups': user_groups}
#     return render(request, 'tienda/todoslosautos.html', context)

@login_required(login_url='logear')
def todos(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        user_groups = list(request.user.groups.all().values_list('name', flat=True))
        orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_cart_items
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = orden['get_cart_items']
    
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Producto.objects.get(id=product_id)
        product.disponible = not product.disponible
        product.save()
        
    context={'productos':productos, 'cartItems':cartItems, 'user_groups': user_groups}
    return render(request, 'tienda/todoslosautos.html', context)

# @login_required(login_url='logear')
# def cambiar_disponibilidad(request, id):
#     producto = get_object_or_404(Producto, id=id)
#     producto.disponible = not producto.disponible
#     producto.save()
#     return redirect('todos')

@login_required(login_url='logear')
def cambiar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        # Check which form was submitted
        if 'cambiar_disponibilidad' in request.POST:
            producto.disponible = not producto.disponible
            producto.save()
        elif 'cambiar_precio' in request.POST:
            nuevo_precio = request.POST.get('nuevo_precio')
            if nuevo_precio:
                producto.precio = float(nuevo_precio)
                producto.save()

        return redirect('todos')

    context = {'producto': producto}
    return render(request, 'tienda/todos.html', context)



def carrito(request):
    
    if request.user.is_authenticated:
        cliente= request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_cart_items
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = orden['get_cart_items']
    context = {'items': items, 'orden':orden, 'cartItems': cartItems}
    return render(request, 'tienda/carrito.html', context)


def clear_cart(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden = Orden.objects.get(cliente=cliente, completado=False)
        productos = orden.ordenproducto_set.all()

        for producto in productos:
            p = Producto.objects.get(id=producto.producto.id)
            p.disponible = True
            p.save()

        productos.delete()
    else:
        cart = json.loads(request.COOKIES.get('cart', '{}'))
        for producto_id in cart:
            p = Producto.objects.get(id=producto_id)
            p.disponible = True
            p.save()
        cart.clear()
        response = JsonResponse({'success': True})
        response.set_cookie('cart', json.dumps(cart))
        return response
    return redirect('tienda')
#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def pago_exitoso(request):
    return render(request, 'tienda/exitoso.html')
def checkout(request):
    if request.user.is_authenticated:
        cliente= request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        items = orden.ordenproducto_set.all()
        cartItems = orden.get_cart_items
        
    else:
        items = []
        orden = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = orden['get_cart_items']
    context={'items':items, 'orden':orden, 'cartItems':cartItems}
    return render(request, 'tienda/checkout.html', context)

def maintienda(request):
    context={}
    return render(request, 'tienda/main.html', context)

def editar(request):
    if request.method == 'POST':
        form = addCarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/tienda')
    else:
        form = addCarForm()
    return render(request, 'tienda/editar.html', {'form': form})

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/tienda')
    return render(request, 'tienda/eliminar.html', {'producto': producto})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:',productId)
    
    cliente = request.user.cliente
    producto = Producto.objects.get(id=productId)
    orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
    ordenproducto, created = OrdenProducto.objects.get_or_create(orden=orden, producto=producto)
    
    if action =='add':
        ordenproducto.cantidad = (ordenproducto.cantidad + 1)
        producto.disponible = False  # Set the product as unavailable
    elif action =='remove':
        ordenproducto.cantidad = (ordenproducto.cantidad - 1)
        producto.disponible = True  # Set the product as available again
    
    ordenproducto.save()
    producto.save()  # Save the updated product
    if ordenproducto.cantidad<=0:
        ordenproducto.delete()
        
    return JsonResponse('Producto fue añadido', safe=False)

#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def processOrder(request):
    id_transaccion= datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        cliente=request.user.cliente
        orden, created= Orden.objects.get_or_create(cliente=cliente, completado=False)
        total=int(data['form']['total'])
        orden.id_transaccion = id_transaccion
        
        if total ==int(orden.get_cart_total):
            orden.completado = True
        orden.save()
        
        
        if orden.shipping==True:
            DireccionEnvio.objects.create(
            cliente=cliente,
            orden=orden,
            direccion=data['shipping']['address'],
            ciudad=data['shipping']['city'],
            region=data['shipping']['state'],
            cpostal=data['shipping']['zipcode'],
            )
    else:
        print('Usuario no esta registrado...')
    return JsonResponse('Pago completado', safe=False)