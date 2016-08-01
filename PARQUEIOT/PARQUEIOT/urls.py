from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
#REST FRAMEWORK-----------------
from rest_framework import routers, serializers, viewsets
from apps.rest.viewset import DispositivoViewSet

router = routers.DefaultRouter()
router.register(r'Dispositivo', DispositivoViewSet)
#
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PARQUEIOT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='sistema'),
    url(r'^dispositivo/',include('apps.dispositivo.urls')),
    url(r'^sensor/',include('apps.sensor.urls')),
    url(r'apirest/', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
)
