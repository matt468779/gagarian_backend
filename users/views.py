from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from users.serializers import UserSerializer
@api_view(['GET', 'POST'])
def all_users(request):
    if (request.method == 'GET'):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "username or password doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"hello": "helloworld"})
        else:
            messages.error(request, "username or password doesn't exist")
        
    return Response(data=user)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    user = User.objects.create()

    