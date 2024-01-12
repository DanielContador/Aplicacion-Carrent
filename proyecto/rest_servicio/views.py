from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from horas.models import Servicio
from rest_servicio.serializers import ServicioSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from horas.forms import ServicioForm

# Create your views here.
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def editarServicio(request, id):
    servicio = Servicio.objects.get(id=id)
    serializer = ServicioSerializer(instance=servicio, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
##@permission_classes((IsAuthenticated,))
def lista_servicio(request):
    if request.method =='GET':
        listaServicio = Servicio.objects.all().order_by('-id')
        serializer = ServicioSerializer(listaServicio, many = True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def crearServicio(request):
    serializer = ServicioSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def eliminarServicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    
    return Response(serializer.data)

"""
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
    except Servicio.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ServicioSerializer(servicio)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        serializer = ServicioSerializer(servicio, data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        servicio.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

"""













"""
METODO VISTO EN CLASES LISTA+POST
@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_servicio(request):
    if request.method =='GET':
        listaServicio = Servicio.objects.all()
        serializer = ServicioSerializer(listaServicio, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = ServicioSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



"""


"""

VISTO EN CLASES GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))

def detalle_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
    except Servicio.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ServicioSerializer(servicio)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        serializer = ServicioSerializer(servicio, data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        servicio.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        """