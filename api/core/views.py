from django.shortcuts import render

from django.contrib.auth.models import User
# Importar viewsets: código pyhton que se encarga de la renderizacion de los elementos en JSON
from rest_framework import viewsets
from core.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
