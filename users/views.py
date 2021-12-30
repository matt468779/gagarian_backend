from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from rest_framework.serializers import Serializer

from users.serializers import CartSerializer, ProductSerializer, UserSerializer
from users.models import Products, Cart, Purchase

from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

@api_view(['GET', 'POST'])
def all_users(request):
    if (request.method == 'GET'):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

def productDetails(request, pk):
    if request.method == 'GET':
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

# @login_required(login_url='rest-auth/')
@api_view(['GET'])
# @authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def carts(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user)
        cartItems = Cart.objects.filter(id=user)
        serializer = CartSerializer(cartItems, many=True)
        data = serializer.data[0]['products']
        return Response(data)

@api_view(['GET'])
# @authentication_classes([SessionAuthentication])
@permission_classes([])
def hello(request):
    user = str(request.user)
    return Response({'hello': user})
