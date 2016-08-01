from django.shortcuts import render
from apps.sistema.models import Sensor,Dispositivo
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


class listarSensor(ListView):
	template_name='sensor/listar.html'
	context_object_name='sensor'
	model=Sensor
	def get_context_data(self, **kwargs):
		ctx = super(listarSensor, self).get_context_data(**kwargs)
		ctx['dispositivo'] = Dispositivo.objects.all()
		ctx['sensor'] = Sensor.objects.all()
		return ctx

class crearSensor(CreateView):
	template_name='sensor/crear.html'
	model=Sensor
	success_url=reverse_lazy('sistema')


class editarSensor(UpdateView):
	model = Sensor
	template_name= 'sensor/editar.html'
	success_url=reverse_lazy('sistema')
#ELIMINAR ARTICULOS
class eliminarSensor(DeleteView):
	model = Sensor
	context_object_name="sensor"
	template_name = 'sensor/eliminar.html'
	success_url = reverse_lazy('sistema')
