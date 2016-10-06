# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.PositiveIntegerField(verbose_name='n\xfamero')),
                ('date_signed', models.DateField(verbose_name='fecha de firma')),
                ('date_termination', models.DateField(verbose_name='fecha de vencimiento')),
                ('payment_type', models.TextField(verbose_name='t\xe9rmino de pago')),
                ('contract_type', models.ForeignKey(related_name='contracts', verbose_name='tipo', to='core.ContractType')),
                ('entity', models.ForeignKey(related_name='contracts', verbose_name='entidad', to='core.Entity')),
            ],
            options={
                'verbose_name': 'contrato',
                'verbose_name_plural': 'contrato',
            },
        ),
    ]
