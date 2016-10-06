# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.snippets.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name='nombre')),
                ('slug', common.snippets.fields.AutoSlugField(editable=False, populate_from='name', allow_duplicates=False, separator='-', blank=True, verbose_name='slug', overwrite=True)),
            ],
            options={
                'verbose_name': 'tipo de contrato',
                'verbose_name_plural': 'tipos de contrato',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name='nombre')),
                ('slug', common.snippets.fields.AutoSlugField(editable=False, populate_from='name', allow_duplicates=False, separator='-', blank=True, verbose_name='slug', overwrite=True)),
            ],
            options={
                'verbose_name': 'entidad',
                'verbose_name_plural': 'entidades',
            },
        ),
    ]
