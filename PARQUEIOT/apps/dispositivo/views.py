#-*- coding: utf-8 -*-
from django.shortcuts import render
from apps.sistema.models import Dispositivo, Sensor
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers
from django.db import transaction
from django.contrib import messages
import json

class listarDispositivo(ListView):
	template_name='dispositivo/listarDispositivo.html'
	context_object_name='dispositivo'
	model=Dispositivo

class crearDispositivo(CreateView):
	template_name='dispositivo/crearDispositivo.html'
	model=Dispositivo
	success_url=reverse_lazy('sistema')


class editarDispositivo(UpdateView):
	model = Dispositivo
	template_name= 'dispositivo/actualizarDispositivo.html'
	success_url=reverse_lazy('sistema')
#ELIMINAR ARTICULOS
class eliminarDispositivo(DeleteView):
	model = Dispositivo
	context_object_name="dispositivo"
	template_name = 'dispositivo/eliminarDispositivo.html'
	success_url = reverse_lazy('sistema')

def delete_post(request):
    if request.method == 'DELETE':

        post = Dispositivo.objects.get(pk=int(QueryDict(request.body).get('postpk')))

        post.delete()

        response_data = {}
        response_data['msg'] = 'Post was deleted.'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def generarDispositivo(request):

    objetosplantilla = {"cuca":1}
    return render_to_response('dispositivo/transaccion.html', objetosplantilla, context_instance=RequestContext(request))





class leerAjax(TemplateView):
    @transaction.atomic
    def get(self,request,*args,**kwargs):
        datos = {}
        d = {}
        data = request.GET['objetos']
        print "********************APARTE******************"     
        d = json.loads(data)
        _transaccion = transaction.savepoint() #crear un punto de referencia para iniciar la transaccion
        try:
            
            for dispo in d["dispositivo"]:
                if(dispo["dispo_nom"] !=""and dispo["dispo_mac"]!=""and dispo["dispo_fabricante"]!=""):
                    nombre_dispositivo = dispo["dispo_nom"]
                    mac_dispositivo = dispo["dispo_mac"]
                    fabricante_dispositivo=dispo["dispo_fabricante"]
                else:
                    raise Exception("Campos Vacios Error de Transacción!")
            #Insercion de Datos en tabla dispositivo
            disp = Dispositivo(dis_mac=mac_dispositivo,dis_nombre=nombre_dispositivo,dis_fabricante=fabricante_dispositivo)
            disp.save()
            disp.id
            id_dispositivo = Dispositivo.objects.get(id=disp.id)
            for s in  d["sensor"]:
                if(s["sensor_nombre"]!="" and s["sensor_mac"] != "" ):
                    sensores = Sensor(sen_nombre=s["sensor_nombre"] ,sen_unidad_medida=s["sensor_mac"],id_dis_id=id_dispositivo.id)
                    sensores.save()
                    
                else:
                    raise Exception("Campos Vacios Error de Transacción!")
            transaction.savepoint_commit(_transaccion) #ejecuta el commit
            datos['result'] = "OK"
            datos['message'] = "¡Registro de dispositivo  guardado correctamente!"
            messages.add_message(request, messages.SUCCESS, datos['message'])
            return HttpResponse(json.dumps(datos), content_type="application/json")
        except Exception as error:
            print("Error al guardar-->transaccion" + str(error))
            transaction.savepoint_rollback(_transaccion)
            datos['message'] = "¡Ha ocurrido un error al tratar de ingresar los datos de la empresa!"
            datos['result'] = "X"
            return HttpResponse(json.dumps(datos), content_type="application/json")

        



def guardarFactura(request):
    print "ASDASDASDASDASDASD"
    #nombre_dispositivo = request['dispo_nombre']
    #print nombre_dispositivo
    #mac_dispositivo = request['mac']
    #fabricante_dispositivo = request['fabricante']
    #sensor_nombre= ['sen_nombre']
    #sensor_unidad= ['sen_unidad']
    #num = request['numero']
    
    

    #data = json.loads(request.POST['json'])
    #for item in data['line_items']:
    #    item['name']

    #if (((int)(num)) == 1):
    #    disp = Dispositivo(dis_mac=mac_dispositivo,dis_nombre=nombre_dispositivo,dis_fabricante=fabricante_dispositivo)
    #    disp.save()
    #    disp.id
    #    print 

    #id_dispositivo = Dispositivo.objects.get(id=dis.id)
    #sensores = Sensor(sen_nombre=sensor_nombre,sen_unidad_medida=sensor_unidad,id_dis_id=id_dispositivo)
    #sensores.save()

    print "******************FIN****************"

    mimetype="application/json"
    return HttpResponse(data_json,mimetype)
