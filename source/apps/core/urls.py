# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    
	url(r'^$', views.SorterView.as_view(), name='sorter'),

    url(r'^panel/$', views.BackendDashboard.as_view(), name='backend_dashboard'),
    url(r'^resumen/$', views.FrontendDashboard.as_view(), name='frontend_dashboard'),

    url(r'^entidades/$', views.EntityList.as_view(), name='entity_list'),
    url(r'^entidades/agregar/$', views.EntityCreate.as_view(), name='entity_create'),
    url(r'^entidades/editar/(?P<pk>\d+)/$', views.EntityUpdate.as_view(), name='entity_update'),
    url(r'^entidades/eliminar/(?P<pk>\d+)/$', views.EntityDelete.as_view(), name='entity_delete'),

    url(r'^tipos-de-contrato/$', views.ContractTypeList.as_view(), name='contract_type_list'),
    url(r'^tipos-de-contrato/agregar/$', views.ContractTypeCreate.as_view(), name='contract_type_create'),
    url(r'^tipos-de-contrato/editar/(?P<pk>\d+)/$', views.ContractTypeUpdate.as_view(), name='contract_type_update'),
    url(r'^tipos-de-contrato/eliminar/(?P<pk>\d+)/$', views.ContractTypeDelete.as_view(), name='contract_type_delete'),
)
