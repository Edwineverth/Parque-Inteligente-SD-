# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_dispositivo_dis_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='dis_fabricante',
            field=models.CharField(max_length=50, verbose_name='Fabricante:'),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='dis_mac',
            field=models.CharField(max_length=17, verbose_name='MAC:'),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='dis_nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre:'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='id_dis',
            field=models.ForeignKey(verbose_name='Dispositivo:', blank=True, to='sistema.Dispositivo', null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sen_nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre:'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sen_unidad_medida',
            field=models.CharField(max_length=10, verbose_name='Unidad de Medida:'),
        ),
    ]
