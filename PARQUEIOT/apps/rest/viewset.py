from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets

from .serializer import DispositivoSerializer
from apps.sistema.models import Dispositivo

class DispositivoViewSet(viewsets.ModelViewSet):
	queryset=Dispositivo.objects.all()
	serializer_class=DispositivoSerializer
