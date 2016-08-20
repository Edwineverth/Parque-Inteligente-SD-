"""SmartPark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from AppPrincipal.views import *
from AppPrincipal.viewSet import *
from django.conf import settings

admin.autodiscover()

router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'parques', ParqueViewSet)
router.register(r'dispositivos', DispositivoViewSet)
router.register(r'sensores', SensorViewSet)

urlpatterns = patterns('',
                       #url(r'^registro/$', registrar, name='Registrar'),
                       
                       url(r'^modulos/pantalla/subirvideo/$', subir_video, name='SubirVideo'),
                       url(r'^modulos/pantalla/$', pantalla, name='Pantalla'),
                       url(r'^modulos/sonido/$', sonido, name='Sonido'),
                       url(r'^modulos/riego/$', riego, name='Riego'),
                       url(r'^moodulos/luz/datos/$', luzDatos, name='LuzDatos' ),
                       url(r'^modulos/luz/$', luz, name='Luz'),
                       url(r'^modulos/$', modulos, name='Modulos'),
                       
                       url(r'modulos/registro/add/$', guardar_registro,name='GuardarRegistro'),
                       url(r'modulos/registro/view/$', ver_registros,name='VerRegistros'),

                       url(r'^administrar/usuarios/new/$', crear_usuario2.as_view(), name='CrearUsuario2'),
                       url(r'^administrar/usuarios/update/(?P<id>\d+)/$', editar_usuario, name='EditarUsuario'),
                       url(r'^administrar/usuarios/delete/(?P<id>\d+)/$', eliminar_usuario, name='EliminarUsuario'),
                       url(r'^administrar/usuarios/activarSuperuser/(?P<id>\d+)/$', activar_superuser, name='ActivarSuperuser'),
                       url(r'^administrar/usuarios/desactivarSuperuser/(?P<id>\d+)/$', desactivar_superuser, name='DesactivarSuperuser'),
                       url(r'^administrar/usuarios/habilitarUser/(?P<id>\d+)/$', habilitar_usuario, name='HabilitarUser'),
                       url(r'^administrar/usuarios/desabilitarUser/(?P<id>\d+)/$', desabilitar_usuario, name='DesabilitarUser'),
                       url(r'^administrar/usuarios/$', admUsuarios, name='AdmUsuarios'),
                       
                       url(r'^administrar/parques/desactivar/(?P<id>\d+)/$', desactivar_parque, name='DesactivarParque'),
                       url(r'^administrar/parques/activar/(?P<id>\d+)/$', activar_parque, name='ActivarParque'),
                       url(r'^administrar/parques/editar/(?P<id>\d+)/$', editar_parque, name='EditarParque'),
                       url(r'^administrar/parques/nuevo/$', nuevo_parque, name='NuevoParque'),
                       url(r'^administrar/parques/$', admParques, name='AdmParques'),

                       url(r'^administrar/sensores/activar/(?P<id>\d+)/$', activar_sensor, name='ActivarSensor'),
                       url(r'^administrar/sensores/desactivar/(?P<id>\d+)/$', desactivar_sensor, name='DesactivarSensor'),
                       url(r'^administrar/sensores/actualizar/(?P<pk>\d+)/$', editar_sensor.as_view(), name='EditarSensor'),
                       url(r'^administrar/sensores/nuevo/$', nuevoSensor, name='NuevoSensor'),
                       url(r'^administrar/sensores/$', admSensores, name='AdmSensores'),
                       
                       url(r'^administrar/dispositivo/nuevo/', nuevoDispositivo, name='NuevoDispositivo'),
                       url(r'^administrar/dispositivo/actualizar/(?P<pk>\d+)/$', editar_dispositivo.as_view(), name='ActualizarDispositivo'),
                       url(r'^administrar/dispositivo/activar/(?P<id>\d+)/$', activar_dispositivo, name='ActivarDispositivo'),
                       url(r'^administrar/dispositivo/desactivar/(?P<id>\d+)/$', desactivar_dispositivo, name='DesactivarDispositivo'),
                       url(r'^administrar/dispositivo/$', admDispositivos, name='AdmDispositivos'),
                       
                       url(r'^crearUsuario/$', crear_usuario.as_view(), name='CrearUsuario1'),
                       url(r'^principal/$', principal, name='Principal'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='Logout'),
                       url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='Login'),
                       # url(r'^/$', login, name='Login'),
                       url(r'rest/', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT,}
                            ),
                       )
