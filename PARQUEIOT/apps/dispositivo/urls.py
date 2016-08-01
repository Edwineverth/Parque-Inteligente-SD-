from django.conf.urls import patterns, include, url
from .views import leerAjax,listarDispositivo,crearDispositivo,editarDispositivo,eliminarDispositivo,generarDispositivo,guardarFactura
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
  
    url(r'^registrar/$', crearDispositivo.as_view(),name='crear_Dispositivo'),
    url(r'^editar/(?P<pk>[\d]+)$', editarDispositivo.as_view(),name='editar_Dispositivo'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarDispositivo.as_view(),name='eliminar_Dispositivo'),
    url(r'^listar/$', listarDispositivo.as_view(),name='listar_Categoria'),
    url(r'^delete_post/$', 'delete_post'),
    url(r'^crear/$', generarDispositivo,name='crearDispositivo'),
    url(r'^crearr/$', guardarFactura,name='crearFacturad'),
    url(r'^ajax/$', leerAjax.as_view(),name='ajaxpeticion'),


    )