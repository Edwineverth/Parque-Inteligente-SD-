# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disp_nombre', models.CharField(max_length=60)),
                ('disp_mac', models.CharField(max_length=17)),
                ('disp_estado', models.CharField(default=b'a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
            ],
        ),
        migrations.CreateModel(
            name='Parque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parq_nombre', models.CharField(max_length=50)),
                ('parq_estado', models.CharField(default=b'a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
            ],
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.CharField(max_length=10)),
                ('parque', models.ForeignKey(to='AppPrincipal.Parque')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_fecha_hora', models.CharField(max_length=100)),
                ('reg_descripcion', models.CharField(max_length=200)),
                ('reg_usuario', models.CharField(max_length=30)),
                ('reg_funcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sen_nombre', models.CharField(max_length=50)),
                ('sen_tipo', models.CharField(max_length=60)),
                ('sen_unidadmedida', models.CharField(max_length=50)),
                ('sen_localizacion', models.CharField(max_length=100)),
                ('sen_estado', models.CharField(default=b'a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
                ('sen_funcion', models.CharField(default=b'a', max_length=1, choices=[('e', 'Encendido'), ('a', 'Apagado')])),
                ('dispositivo', models.ForeignKey(to='AppPrincipal.Dispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('video', models.FileField(upload_to=b'videos/')),
            ],
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='parque',
            field=models.ForeignKey(to='AppPrincipal.Parque'),
        ),
    ]
