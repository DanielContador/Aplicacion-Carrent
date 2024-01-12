from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from horas.models import Perfil



@api_view(['POST'])
def login(request):

    #esto se debe reemplazar por el HTML
    #data = JSONParser().parse(request)
    username = request.POST['username'] #data['username']
    password = request.POST['password'] #data['password']
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        #esto traducirlo a que se muestre por el html
        return Response("Usuario Inválido")

    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password Incorrecta")
    token, created = Token.objects.get_or_create(user=user)
    return redirect(to='index')
    

"""
@api_view(['POST'])
def login(request):
    #esto se debe reemplazar por el HTML
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        #esto traducirlo a que se muestre por el html
        return Response("Usuario Inválido")

    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password Incorrecta")


    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)


"""