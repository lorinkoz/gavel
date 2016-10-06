# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta

from django.db import models
from django.conf import settings
from django.core.validators import ValidationError
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Contract(models.Model):
    
    uid = models.PositiveIntegerField(verbose_name='número')

    entity = models.ForeignKey('core.Entity', verbose_name='entidad', related_name='contracts')
    contract_type = models.ForeignKey('core.ContractType', verbose_name='tipo', related_name='contracts')
    notes = models.TextField(verbose_name='notas', blank=True)

    date_signed = models.DateField(verbose_name='fecha de firma')
    date_termination = models.DateField(verbose_name='fecha de vencimiento')

    payment_type = models.CharField(verbose_name='término de pago', max_length=1024)

    class Meta:
        verbose_name = 'contrato'
        verbose_name_plural = 'contrato'

    def __str__(self):
        return '%d' % self.uid

    def clean(self):
        if self.date_termination <= self.date_signed:
            raise ValidationError('La fecha de vencimiento debe ser posterior a la fecha de firma')

    @property
    def html_id(self):
        return str(self)

    @property
    def is_aged(self):
        now = timezone.localtime(timezone.now())
        return now.date() <= self.date_termination < timezone.localtime(now + timedelta(days=settings.AGED_LIMIT)).date()

    @property
    def is_terminated(self):
        return self.date_termination < timezone.localtime(timezone.now()).date()

    def expiration_countdown(self):
        delta = self.date_termination - self.date_signed
        return delta.days
    expiration_countdown.verbose_name = 'días para vencimiento'

    # TODO: Convert these methods into new query methods
    # Change accordingly in related views

    @staticmethod
    def get_aged(base_queryset=None):
        queryset = base_queryset or Contract.objects.all()
        now = timezone.now()
        limit = now + timedelta(days=settings.AGED_LIMIT)
        return queryset.filter(date_termination__gte=now, date_termination__lte=limit)

    @staticmethod
    def get_terminated(base_queryset=None):
        queryset = base_queryset or Contract.objects.all()
        return queryset.filter(date_termination__lt=timezone.now())