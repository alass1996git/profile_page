from django.http import HttpResponse
from django.shortcuts import render
import rest_framework
from rest_framework import generics
from . import serializers
from .models import menuModel

def sayHello(request):
    return HttpResponse('Hello Worlds')

def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = menuModel.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menuModel.objects.all()
    serializer_class = serializers.MenuSerializer