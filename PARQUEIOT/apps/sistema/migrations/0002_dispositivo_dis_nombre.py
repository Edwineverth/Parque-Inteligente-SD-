# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='dis_nombre',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
