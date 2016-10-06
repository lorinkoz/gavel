# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from common.admin import myadmin

from . import models


@admin.register(models.Contract, site=myadmin)
class ContractAdmin(admin.ModelAdmin):
    search_fields = ('uid', 'entity', 'contract_type', 'payment_type')
    list_display = ('uid', 'entity', 'contract_type', 'date_signed', 'date_termination', 'expiration_countdown')
