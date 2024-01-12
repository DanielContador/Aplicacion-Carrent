from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    patente = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    ndepuertas=models.IntegerField()
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nombre
    ##property, hace que la pagina no se caiga si
    ##no se agrega una imagen al producto
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url
    
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    id_transaccion = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    

    
    
    @property
    def get_cart_total(self):
        ordenproducto = self.ordenproducto_set.all()
        total = sum([item.get_total for item in ordenproducto])
        return total
    
    @property
    def get_cart_items(self):
        ordenproducto = self.ordenproducto_set.all()
        total = sum([item.cantidad for item in ordenproducto])
        return total
        
            # @property
    # def shipping(self):
    #     shipping = False
    #     ordenproducto = self.ordenproducto_set.all()
    #     for i in ordenproducto:
    #         if i.producto.digital == False:
    #             shipping = True
    #     return shipping
    
class OrdenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden,on_delete=models.SET_NULL, null=True, related_name='ordenproducto_set')
    cantidad = models.IntegerField(default=0, null=True,blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total
    
    
class DireccionEnvio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=200, null=False)
    ciudad = models.CharField(max_length=200, null=False)
    region = models.CharField(max_length=200, null=False)
    cpostal = models.CharField(max_length=200, null=False)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion