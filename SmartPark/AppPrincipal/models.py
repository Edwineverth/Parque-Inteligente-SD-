from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.



class Parque(models.Model):
    parq_nombre = models.CharField(max_length=50)
    EST_CHOICES = (
        (u'a', u'Activo'),
        (u'i', u'Inactivo'),
    )
    parq_estado = models.CharField(max_length=1, choices=EST_CHOICES, default='a')
    def __str__(self):
        return self.parq_nombre

class Perfiles(models.Model):
    usuario = models.OneToOneField(User)
    parque = models.ForeignKey(Parque)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.usuario.username

class Dispositivo(models.Model):
    disp_nombre = models.CharField(max_length=60)
    disp_mac = models.CharField(max_length=17)
    EST_CHOICES = (
        (u'a', u'Activo'),
        (u'i', u'Inactivo'),
    )
    disp_estado = models.CharField(max_length=1, choices=EST_CHOICES, default='a')
    parque = models.ForeignKey(Parque)
    def __str__(self):
        return self.disp_nombre

class Sensor(models.Model):
    sen_nombre = models.CharField(max_length=50)
    sen_tipo = models.CharField(max_length=60)
    sen_unidadmedida=models.CharField(max_length=50)
    sen_localizacion=models.CharField(max_length=100)
    FUN_CHOICES = (
        (u'e', u'Encendido'),
        (u'a', u'Apagado'),
    )
    EST_CHOICES = (
        (u'a', u'Activo'),
        (u'i', u'Inactivo'),
    )
    sen_estado = models.CharField(max_length=1, choices=EST_CHOICES, default='a')
    sen_funcion = models.CharField(max_length=1, choices=FUN_CHOICES, default='a')
    dispositivo = models.ForeignKey(Dispositivo)
    def __str__(self):
        return self.sen_nombre

class Registro(models.Model):
    reg_fecha_hora =  models.CharField(max_length=100)
    reg_descripcion = models.CharField(max_length=200)
    reg_usuario = models.CharField(max_length=30)
    reg_funcion=models.CharField(max_length=30)
    def __str__(self):
        return self.reg_descripcion

class Video(models.Model):
    title = models.CharField(max_length=300)
    video = models.FileField(upload_to='videos/')
    def __str__():
        return self.title