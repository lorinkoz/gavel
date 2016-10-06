# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='notes',
            field=models.TextField(verbose_name='notas', blank=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='payment_type',
            field=models.CharField(max_length=1024, verbose_name='t\xe9rmino de pago'),
        ),
    ]
