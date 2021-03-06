from django.shortcuts import render
from AppPrincipal.models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import viewsets


"""class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()


class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()"""

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

class ParqueViewSet(viewsets.ModelViewSet):
	serializer_class = ParqueSerializer
	queryset = Parque.objects.all()

class DispositivoViewSet(viewsets.ModelViewSet):
	serializer_class = DispositivoSerializer
	queryset = Dispositivo.objects.all()

class TipoSensorViewSet(viewsets.ModelViewSet):
	serializer_class = TipoSensorSerializer
	queryset = TipoSensor.objects.all()

class SensorViewSet(viewsets.ModelViewSet):
	serializer_class = SensorSerializer
	queryset = Sensor.objects.all()

class AccionSensorViewSet(viewsets.ModelViewSet):
	serializer_class = AccionSensorSerializer
	queryset = AccionSensor.objects.all()

class RegistroViewSet(viewsets.ModelViewSet):
	serializer_class = RegistrosSerializer
	queryset = Registro.objects.all()

class PublicidadViewSet(viewsets.ModelViewSet):
	serializer_class = PublicidadSerializer
	queryset = Publicidad.objects.all()