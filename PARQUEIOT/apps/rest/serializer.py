from rest_framework import serializers
from django.contrib.auth.models import User
from apps.sistema.models import Dispositivo

class DispositivoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model= Dispositivo
		fields=('id','dis_nombre','dis_mac','dis_fabricante',)
