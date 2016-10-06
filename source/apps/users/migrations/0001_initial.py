# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='correo electr\xf3nico')),
                ('display_name', models.CharField(max_length=50, verbose_name='nombre', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('role', models.PositiveIntegerField(default=0, verbose_name='rol', choices=[(0, 'Inactivo'), (1, 'Consultor'), (2, 'Operador'), (3, 'Administrador')])),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]
