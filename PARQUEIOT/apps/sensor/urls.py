from django.conf.urls import patterns, include, url
from .views import listarSensor,crearSensor,editarSensor,eliminarSensor
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
  
    url(r'^registrar/$', crearSensor.as_view(),name='crear_sensor'),
    url(r'^editar/(?P<pk>[\d]+)$', editarSensor.as_view(),name='editar_sensor'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarSensor.as_view(),name='eliminar_sensor'),
    url(r'^listar/$', listarSensor.as_view(),name='listar_Sensor'),

    )