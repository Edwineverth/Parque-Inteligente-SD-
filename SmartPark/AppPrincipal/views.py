from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .form import UserForm, DispositivoForm, DispositivoEditForm, SensorForm, UserForm1, UserForm2, VideoForm, UserEditForm, ParqueForm
from django.core import serializers
from django.core.serializers import json
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, render_to_response,redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic import FormView, UpdateView, TemplateView, DetailView
from datetime import *
from django.utils import timezone
import paho.mqtt.client as paho
from django.conf import settings
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
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

def riego(request):
    return render_to_response('riego.html', '', context_instance=RequestContext(request))
#@login_required(login_url='/')
#@csrf_exmpt
def sonido(request):
    return render_to_response('sonido.html', '', context_instance=RequestContext(request))

def pantalla(request):
    return render_to_response('pantalla.html', '', context_instance=RequestContext(request))

def subir_video(request):
    #codigo alternativo pa probar
    """mymodel = Mymodel.objects.get(id=1)
    file_content = ContentFile(request.FILES['video'].read())
    mymodel.video.save(request.FILES['video'].name, file_content)"""
    if request.POST:
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pantalla')
    else:
        form = VideoForm()
    return render_to_response('subirVideo.html', {'form': form}, context_instance=RequestContext(request))



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
    fields=('disp_nombre','disp_mac','parque')
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

#A-----------DMINISTRAR USUARIOS-------------#
@login_required(login_url='/')
def admUsuarios(request):
    usuarios = User.objects.all()
    perfil = Perfiles.objects.all()
    return render_to_response('AdmUsuario.html', {'usuarios':usuarios, 'perfil':perfil}, context_instance=RequestContext(request))

@login_required(login_url='/')
def editar_usuario(request,id):
    parques=Parque.objects.all()
    usuario=get_object_or_404(User,pk=id)
    try:
        perfil=get_object_or_404(Perfiles,usuario=usuario)
    except Exception, e:
        print(e)
        perfil=Perfiles()
    cont={'parques':parques,'usuario':usuario,'perfil':perfil}
    print(perfil.parque)
    if request.method=='POST':
        try:
            with transaction.atomic():
                print("entro try")
                usuario = User(id=id,
                                username=request.POST['txtUsername'],
                                first_name=request.POST['txtFirstname'],
                                last_name=request.POST['txtLastname'],
                                email=request.POST['txtEmail'],
                                )
                
                print(request.POST['txtId'])
                print(usuario.id)
                perfil = Perfiles(id=id_perfil,
                                    usuario=usuario.id,
                                    parque=request.POST['selectParque'],
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
    user.is_active=False
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

#sid = transaction.savepoint()
#transaction.savepoint_commit(sid)

def registrar(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                parque = Parque(parq_nombre=request.POST['txtNombrePark'])
                parque.save()
                print(parque.parq_nombre)
                dispositivo = Dispositivo(parque_id=parque.id,
                                          disp_nombre=request.POST['txtNombreDisp'],
                                          disp_mac=request.POST['txtMacDisp'])
                dispositivo.save()
                print(dispositivo.disp_nombre)
                print(dispositivo.disp_mac)
                sensor = Sensor(dispositivo_id=dispositivo.id,
                                sen_nombre=request.POST['txtNombreSen'],
                                sen_tipo=request.POST['txtTipoSen']
                                )
                sensor.save()
                # serializado = json.dumps(["Ha guardado correctamente los datos de "+ "success"])
                return redirect('Login')
        except Exception as e:
            return render_to_response('FormularioRegistrar.html', '', context_instance=RequestContext(request))
    return render_to_response('FormularioRegistrar.html', '', context_instance=RequestContext(request))

