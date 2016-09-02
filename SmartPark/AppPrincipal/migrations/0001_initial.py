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
            name='AccionSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc_nombre', models.CharField(max_length=50)),
                ('acc_fecha_hora', models.CharField(max_length=110)),
                ('acc_atributo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disp_nombre', models.CharField(max_length=60)),
                ('disp_mac', models.CharField(max_length=17)),
                ('dis_idred', models.CharField(max_length=30)),
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
            name='Publicidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_title', models.CharField(max_length=300)),
                ('pub_imagen', models.ImageField(upload_to=b'imagenes/')),
                ('parque', models.ForeignKey(to='AppPrincipal.Parque')),
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
                ('sen_unidadmedida', models.CharField(max_length=50)),
                ('sen_localizacion', models.CharField(max_length=100)),
                ('sen_estado', models.CharField(default=b'a', max_length=1, choices=[('a', 'Activo'), ('i', 'Inactivo')])),
                ('dispositivo', models.ForeignKey(to='AppPrincipal.Dispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='TipoSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tip_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('dispositivo', models.ForeignKey(to='AppPrincipal.Dispositivo')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='tipo',
            field=models.ForeignKey(to='AppPrincipal.TipoSensor'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='parque',
            field=models.ForeignKey(to='AppPrincipal.Parque'),
        ),
        migrations.AddField(
            model_name='accionsensor',
            name='sensor',
            field=models.ForeignKey(to='AppPrincipal.Sensor'),
        ),
    ]
