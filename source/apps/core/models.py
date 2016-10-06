# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.core.validators import ValidationError
from django.utils.encoding import python_2_unicode_compatible

from common.snippets import fields as snippets


@python_2_unicode_compatible
class Entity(models.Model):
    
    name = models.CharField(verbose_name='nombre', max_length=512)
    slug = snippets.AutoSlugField(verbose_name='slug', populate_from='name', overwrite=True)

    class Meta:
        verbose_name = 'entidad'
        verbose_name_plural = 'entidades'

    def __str__(self):
        return self.name

    @property
    def html_id(self):
        return '%d' % self.pk


class ContractType(models.Model):

    name = models.CharField(verbose_name='nombre', max_length=512)
    slug = snippets.AutoSlugField(verbose_name='slug', populate_from='name', overwrite=True)
    
    class Meta:
        verbose_name = 'tipo de contrato'
        verbose_name_plural = 'tipos de contrato'

    def __str__(self):
        return self.name

    @property
    def html_id(self):
        return '%d' % self.pk