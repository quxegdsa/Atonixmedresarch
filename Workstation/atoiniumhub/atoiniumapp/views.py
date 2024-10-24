from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

def home(request):
    return HttpResponse("Welcome to the Home Page!")

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer