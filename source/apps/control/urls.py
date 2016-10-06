# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    
    url(r'^contratos/$', views.ContractList.as_view(), name='contract_list'),
    url(r'^contratos/proximos-a-vencerse/$', views.AgedContractList.as_view(), name='aged_contract_list'),
    url(r'^contratos/vencidos/$', views.TerminatedContractList.as_view(), name='terminated_contract_list'),
    url(r'^contratos/agregar/$', views.ContractCreate.as_view(), name='contract_create'),
    url(r'^contratos/editar/(?P<pk>\d+)/$', views.ContractUpdate.as_view(), name='contract_update'),
    url(r'^contratos/eliminar/(?P<pk>\d+)/$', views.ContractDelete.as_view(), name='contract_delete'),
)
