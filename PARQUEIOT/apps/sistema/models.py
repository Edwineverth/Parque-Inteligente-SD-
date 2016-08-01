
from __future__ import unicode_literals

from django.db import models


class Dispositivo(models.Model):
    
    dis_nombre = models.CharField(max_length=50,verbose_name=u"Nombre:",null=False,blank=False)
    dis_mac = models.CharField(max_length=17,verbose_name=u"MAC:",null=False,blank=False)
    dis_fabricante = models.CharField(max_length=50,verbose_name=u"Fabricante:",null=False,blank=False)

    class Meta:
        ordering = ["id"]
    def __unicode__(self):
		return self.dis_nombre


class Sensor(models.Model):
   
    sen_nombre = models.CharField(max_length=50,verbose_name=u"Nombre:")
    sen_unidad_medida = models.CharField(max_length=10,verbose_name=u"Unidad de Medida:")
    id_dis = models.ForeignKey(Dispositivo, blank=True, null=True,verbose_name=u"Dispositivo:")  # Field name made lowercase.

    class Meta:
        ordering = ["id"]
    def __unicode__(self):
		return self.sen_nombre
