# serialiacion : tomar objetos de Python y convertirlos a código Javascript

# Importar la clase User
from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
# importar desde restframework -> serializers
from rest_framework import serializers


# Crear una clase User
class UserSerializer(serializers.ModelSerializer):
    class Meta: # subclase meta: que cosas se van a utilziar dentro de la interfaz
        model = User
        fields = ("username","email")

