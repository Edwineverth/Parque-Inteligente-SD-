from rest_framework import serializers
from AppPrincipal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

"""class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'nombre', 'editorial', 'genero', 'autor',)

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'apellido',)"""

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','password','email')

class ParqueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parque
		fields = ('id','parq_nombre','parq_estado')

class DispositivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dispositivo
		fields = ('id','disp_nombre','disp_mac','disp_estado','parque')

class TipoSensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoSensor
		fields = ('id','tip_nombre')

class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensor
		fields = ('id','sen_nombre','sen_unidadmedida','sen_localizacion','sen_tipo','sen_estado','dispositivo')

class AccionSensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = AccionSensor
		fields= ('id','acc_nombre','acc_fecha_hora','acc_atributo','sensor')

class RegistrosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registro
		fields = ('id','reg_fecha_hora','reg_descripcion','reg_usuario','reg_funcion')

class PublicidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Publicidad
		fields = ('pub_title','pub_imagen','parque')	