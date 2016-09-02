from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .form import *
from django.core import serializers
from django.core.serializers import json
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic import FormView, UpdateView, TemplateView, DetailView
from django.http import HttpResponse
from datetime import *
from django.utils import timezone
import paho.mqtt.client as paho
from django.conf import settings
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives

import json

import paho.mqtt.client as mqtt
import random
import time
# Create your views here.

#LOGIN
def login(request):
    if request.method=='POST':
        cedula = request.method['txtcedula']
        password = request.method['txtpassword']
    return render_to_response('login.html','',context_instance=RequestContext(request))



@login_required(login_url='/')
def principal(request):
    return render_to_response('principal.html', '', context_instance=RequestContext(request))


#-------------MODULOS-------------#
@login_required(login_url='/')
def modulos(request):
    return render_to_response('modulos.html', '', context_instance=RequestContext(request))

@login_required(login_url='/')
def luz(request):
    return render_to_response('luz.html', '', context_instance=RequestContext(request))

def luzDatos(request):
    mqttc = paho.Client()
    host = "192.168.0.103"
    topic = ""
    port = 1883
    #callbacks
    def on_connect(mosq,obj,rc):
        print("conect rc: "+str(rc))
        mqttc.publish("Ejemplo","Python  Script Test Message")
    def on_message(mosq,obj, msg):
        print("Recibiendo topico: "+msg.topic + "Mensaje: "+str(msg.payload)+"\n")
    def on_subscribe(mosq, obj, mid, granted_qos):
        print("Subscribed OK")
    mqttc.on_message = on_message()
    mqttc.on_connect = on_connect()
    mqttc.on_subscribe = on_subscribe()
    #conect and subscribe
    mqttc.connect(host, port, 60)
    mqttc.subscribe(topic,0)
    return render_to_response('luzDatos.html', '', context_instance=RequestContext(request))

@login_required(login_url='/')
def riego(request):
    return render_to_response('riego.html', '', context_instance=RequestContext(request))
#@login_required(login_url='/')
#@csrf_exmpt
@login_required(login_url='/')
def sonido(request):
    return render_to_response('sonido.html', '', context_instance=RequestContext(request))

@login_required(login_url='/')
def pantalla(request):
    imagenes = Imagen.objects.all()
    return render_to_response('pantalla.html', {'imagenes':imagenes}, context_instance=RequestContext(request))

@login_required(login_url='/')
def subir_imagen(request):
    if request.POST:
        form = PublicidadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Pantalla')
    else:
        form = PublicidadForm()
    return render_to_response('subirImagen.html', {'form': form}, context_instance=RequestContext(request))



#----------------------------------ADMINISTRAR-------------#

#--------ADMINISTRAR PARQUES-------#
@login_required(login_url='/')
def admParques(request):
    parques = Parque.objects.all()
    return render_to_response('AdmParque.html', {'parques':parques}, context_instance=RequestContext(request))

@login_required(login_url='/')
def nuevo_parque(request):
    if request.POST:
        form = ParqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdmParques')
    else:
        form = ParqueForm()
    return render_to_response('ingresoParque.html', {'form': form}, context_instance=RequestContext(request))

@login_required(login_url='/')
def editar_parque(request,id):
    parque = get_object_or_404(Parque,pk=id)
    if request.method=='POST':
        parque=Parque(id=id,parq_nombre=request.POST['txtNombre'],parq_estado=parque.parq_estado,)
        parque.save()
        return redirect('AdmParques')
    return render_to_response('editarParque.html',{'parque':parque}, context_instance=RequestContext(request))

@login_required(login_url='/')
def activar_parque(request,id):
    parque = Parque.objects.get(id=id)
    parque.parq_estado='a'
    parque.save()
    return redirect('AdmParques')

@login_required(login_url='/')
def desactivar_parque(request,id):
    parque = Parque.objects.get(id=id)
    parque.parq_estado='i'
    parque.save()
    return redirect('AdmParques')


#----------ADMINISTRAR DISPOSITIVOS---------#
@login_required(login_url='/')
def admDispositivos(request):
    dispositivos = Dispositivo.objects.all()
    parques = Parque.objects.all()
    return render_to_response('AdmDispositivo.html', {'dispositivos':dispositivos, 'parques':parques}, context_instance=RequestContext(request))

@login_required(login_url='/')
def nuevoDispositivo(request):
    if request.POST:
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdmDispositivos')
    else:
        form = DispositivoForm()
    return render_to_response('ingresoDispositivo.html', {'form': form}, context_instance=RequestContext(request))

class editar_dispositivo(UpdateView):
    model=Dispositivo
    fields=('disp_nombre','disp_mac','dis_idred','parque')
    #form_class=DispositivoEditForm
    template_name='editarDispositivo.html'
    success_url='/administrar/dispositivo/'

@login_required(login_url='/')
def activar_dispositivo(request,id):
    dispositvo = Dispositivo.objects.get(id=id)
    dispositvo.disp_estado='a'
    dispositvo.save()
    return redirect('AdmDispositivos')

@login_required(login_url='/')
def desactivar_dispositivo(request,id):
    dispositvo = Dispositivo.objects.get(id=id)
    dispositvo.disp_estado='i'
    dispositvo.save()
    return redirect('AdmDispositivos')

#-----------ADMINISTRAR TIPO DE SENSORES-------#
@login_required(login_url='/')
def admTipoSensores(request):
    tipo_sensores = TipoSensor.objects.all()
    return render_to_response('AdmTipoSensor.html', {'tipo_sensores':tipo_sensores}, context_instance=RequestContext(request))

@login_required(login_url='/')
def nuevoTipoSensor(request):
    if request.POST:
        form = TipoSensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdmTipoSensores')
    else:
        form = TipoSensorForm()
    return render_to_response('ingresoTipoSensor.html', {'form': form}, context_instance=RequestContext(request))

class editar_tiposensor(UpdateView):
    model=TipoSensor
    fields=('tip_nombre',)
    template_name='editarTipoSensor.html'
    success_url='/administrar/tiposensores/'

#-----------ADMINISTRAR TOPICOS-------#
@login_required(login_url='/')
def admTopicos(request):
    topicos = Topico.objects.all()
    return render_to_response('AdmTopico.html', {'topicos':topicos}, context_instance=RequestContext(request))

@login_required(login_url='/')
def nuevoTopico(request):
    if request.POST:
        form = TopicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdmTopicos')
    else:
        form = TopicoForm()
    return render_to_response('ingresoTopico.html', {'form': form}, context_instance=RequestContext(request))

class editar_topico(UpdateView):
    model = Topico
    fields=('url','dispositivo')
    template_name='editarTopico.html'
    success_url='/administrar/topicos/'

@login_required(login_url='/')
def eliminar_topico(request,id):
    topico = Topico.objects.get(id=id)
    topico.delete()
    return redirect('AdmTopicos')

#----------ADMINISTRAR SENSORES--------------#
@login_required(login_url='/')
def admSensores(request):
    sensores = Sensor.objects.all()
    dispositivos = Dispositivo.objects.all()
    return render_to_response('AdmSensor.html', {'sensores':sensores,'dispositivos':dispositivos}, context_instance=RequestContext(request))

@login_required(login_url='/')
def nuevoSensor(request):
    if request.POST:
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdmSensores')
    else:
        form = SensorForm()
    return render_to_response('ingresoSensor.html', {'form': form}, context_instance=RequestContext(request))

class editar_sensor(UpdateView):
    model=Sensor
    fields=('sen_nombre','sen_unidadmedida','sen_localizacion','sen_tipo','dispositivo')
    template_name='editarSensor.html'
    success_url='/administrar/sensores/'

@login_required(login_url='/')
def activar_sensor(request,id):
    sensor = Sensor.objects.get(pk=id)
    sensor.sen_estado='a'
    sensor.save()
    return redirect('AdmSensores')

@login_required(login_url='/')
def desactivar_sensor(request,id):
    sensor = Sensor.objects.get(pk=id)
    sensor.sen_estado='i'
    sensor.save()
    return redirect('AdmSensores')

#-----------ADMINISTRAR USUARIOS-------------#
@login_required(login_url='/')
def admUsuarios(request):
    usuarios = User.objects.all()
    perfil = Perfiles.objects.all()
    return render_to_response('AdmUsuario.html', {'usuarios':usuarios, 'perfil':perfil}, context_instance=RequestContext(request))

@login_required(login_url='/')
def editar_usuario(request,id):
    parques=Parque.objects.all()
    usuario=get_object_or_404(User,pk=id)
    cont={}
    perfil=""
    n=False
    try:
        perf=get_object_or_404(Perfiles,usuario=usuario)
        id_perfil=perf.id
        perfil=perf
    except Exception, e:
        print(e)
        n=True
    cont={'parques':parques,'usuario':usuario,'perfil':perfil}
    if request.method=='POST':
        try:
            with transaction.atomic():
                print("entro try")
                usuario = User(id=id,
                                username=request.POST['txtUsername'],
                                password=usuario.password,
                                is_superuser=usuario.is_superuser,
                                first_name=request.POST['txtFirstname'],
                                last_name=request.POST['txtLastname'],
                                email=request.POST['txtEmail'],
                                is_staff=usuario.is_staff,
                                is_active=usuario.is_active,
                                )
                parq=Parque.objects.get(pk=request.POST['selectParque'])
                if n==True:
                    print("nuevo perfil")
                    perfil=Perfiles(usuario=usuario,
                        parque=parq,
                        telefono=request.POST['txtTelefono']
                        )
                else:
                    print("editar perfil")
                    perfil = Perfiles(id=id_perfil,
                                        usuario=usuario,
                                        parque=parq,
                                        telefono=request.POST['txtTelefono'],
                                        )
                usuario.save()
                perfil.save()
                print("listo")
                return redirect('AdmUsuarios')
        except Exception, e:
            return render_to_response('editarUsuario.html', cont, context_instance=RequestContext(request))
    return render_to_response('editarUsuario.html', cont, context_instance=RequestContext(request))    

@login_required(login_url='/')
def eliminar_usuario(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('AdmUsuarios')

@login_required(login_url='/')
def activar_superuser(request,id):
    user = get_object_or_404(User,pk=id)
    user.is_superuser=True
    user.save()
    return redirect('AdmUsuarios')

@login_required(login_url='/')
def desactivar_superuser(request,id):
    user = get_object_or_404(User,pk=id)
    user.is_superuser=False
    user.save()
    return redirect('AdmUsuarios')

@login_required(login_url='/')
def habilitar_usuario(request,id):
    user = get_object_or_404(User,pk=id)
    user.is_active=True
    user.save()
    return redirect('AdmUsuarios')

@login_required(login_url='/')
def desabilitar_usuario(request,id):
    user = get_object_or_404(User,pk=id)
    user.is_active=False
    user.save()
    return redirect('AdmUsuarios')


class crear_usuario2(FormView):
    template_name = 'ingresoUsuario2.html'
    form_class = UserForm
    success_url = reverse_lazy('AdmUsuarios')
    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = form.save()
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.is_superuser = form.cleaned_data['is_superuser']
                user.is_staff = form.cleaned_data['is_staff']
                user.is_active = form.cleaned_data['is_active']
                user.save()
                perfil = Perfiles()
                print(""+str(user))
                perfil.usuario = user
                print(""+str(user.id))
                perfil.telefono = form.cleaned_data['telefono']
                print(""+str(perfil.telefono))
                perfil.parque = form.cleaned_data['parque']
                perfil.save()
                return super(crear_usuario2, self).form_valid(form)
        except Exception as e:
            return redirect('CrearUsuario2')

class crear_usuario(FormView):
    form_class = UserCreationForm
    template_name = 'ingresoUsuario1.html'
    success_url ='/'
    def form_valid(self, form):
        form.save()
        return super(crear_usuario, self).form_valid(form)


#-----------------------------------------------#

def ver_registros(request):
    registros=Registro.objects.all()
    return render_to_response('VerRegistros.html', {'registros':registros}, context_instance=RequestContext(request))    


def guardar_registro(request):
    registro=Registro(reg_fecha_hora=datetime.now(),
        reg_descripcion=request.GET['descripcion'],
        reg_usuario=request.user.username,
        reg_funcion=request.GET['funcion']
        )
    registro.save()
    asunto = 'SMARTPARK'
    mensaje = "El Servicio de SMARTPARK le notifica que habido actividad:"\
              + "\n" + request.GET['descripcion'] + "por el usuario "+ request.user.username
    remitente = settings.EMAIL_HOST_USER
    destino = "jglojan@gmail.com"
    #send_mail(asunto,mensaje,remitente,[destino],fail_silently=False)
    email = EmailMessage(asunto,mensaje,to=[destino])
    email.send()
    print("exito")


class mqttluces(TemplateView):
    def get(self,request,*args,**kwargs):
        mensajes_Error = {}
        datosJson = {}
        try:
            data = request.GET['objetos']
            timestamp = int(time.time())
            broker = '192.168.1.6'
            port = 1883
            datosJson = json.loads(data)
            #*********************MQTT PUBLICADOR******************
            topic = 'sensor/luminico'
            message = datosJson['valor']
            mqttclient = mqtt.Client("mqtt-panel-test", protocol=mqtt.MQTTv311)
            mqttclient.connect(broker, port=int(port))
            mqttclient.publish(topic, message)
            #time.sleep(2)
            mensajes_Error['message'] = "Se ha publicado un mensaje en el topico SENSOR/luminico"
            mensajes_Error['result'] = "OK"
            return HttpResponse(json.dumps(mensajes_Error), content_type="application/json")
        except Exception as error:
            print("Error al guardar-->transaccion" + str(error))
            mensajes_Error['message'] = "Ha ocurrod un error al publicar"
            mensajes_Error['result'] = "X"
            return HttpResponse(json.dumps(mensajes_Error), content_type="application/json")
