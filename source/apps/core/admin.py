# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from common.admin import myadmin

from . import models


@admin.register(models.Entity, site=myadmin)
class EntityAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    readonly_fields = ('slug',)


@admin.register(models.ContractType, site=myadmin)
class ContractTypeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    readonly_fields = ('slug',)