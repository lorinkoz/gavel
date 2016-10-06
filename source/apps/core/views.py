# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone

from braces.views import SetHeadlineMixin

from . import models
from apps.control.models import Contract
from common.mixins import ConsultorRequiredMixin, StaffRequiredMixin


class SorterView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        user = self.request.user
        if user.is_anonymous():
            return reverse(settings.LOGIN_URL)
        else:
            return reverse(user.get_absolute_url())


class BackendDashboard(StaffRequiredMixin, SetHeadlineMixin, TemplateView):
    headline = 'Panel de control'
    template_name = 'core/dashboard_backend.html'

    def get_context_data(self, **kwargs):
        context = super(BackendDashboard, self).get_context_data(**kwargs)
        context['aged_contracts'] = Contract.get_aged().count()
        context['terminated_contracts'] = Contract.get_terminated().count()
        return context


class FrontendDashboard(ConsultorRequiredMixin, SetHeadlineMixin, TemplateView):
    template_name = 'core/dashboard_frontend.html'

    def get_context_data(self, **kwargs):
        context = super(FrontendDashboard, self).get_context_data(**kwargs)
        return context


class EntityList(StaffRequiredMixin, SetHeadlineMixin, ListView):
    model = models.Entity
    paginate_by = 25
    page_kwarg = 'p'
    headline = 'Entidades'
    template_name = 'core/entity_list.html'

    def get_queryset(self):
        queryset = super(EntityList, self).get_queryset()
        query = self.request.GET.get('q','')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class EntityCreate(StaffRequiredMixin, SetHeadlineMixin, CreateView):
    model = models.Entity
    fields = '__all__'
    headline = 'Nueva entidad'
    template_name = 'core/entity_form.html'

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('entity_list'))


class EntityUpdate(StaffRequiredMixin, SetHeadlineMixin, UpdateView):
    model = models.Entity
    fields = '__all__'
    headline = 'Editar entidad %s'
    template_name = 'core/entity_form.html'
    
    def get_headline(self):
        return self.headline % self.get_object()

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('entity_list'))


class EntityDelete(StaffRequiredMixin, SetHeadlineMixin, DeleteView):
    model = models.Entity
    headline = 'Eliminar entidad %s'
    template_name = 'core/entity_delete.html'

    def get_headline(self):
        return self.headline % self.get_object()

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('entity_list'))


class ContractTypeList(StaffRequiredMixin, SetHeadlineMixin, ListView):
    model = models.ContractType
    paginate_by = 25
    page_kwarg = 'p'
    headline = 'Tipos de contrato'
    template_name = 'core/contract_type_list.html'

    def get_queryset(self):
        queryset = super(ContractTypeList, self).get_queryset()
        query = self.request.GET.get('q','')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class ContractTypeCreate(StaffRequiredMixin, SetHeadlineMixin, CreateView):
    model = models.ContractType
    fields = '__all__'
    headline = 'Nuevo tipo de contrato'
    template_name = 'core/contract_type_form.html'

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('contract_type_list'))


class ContractTypeUpdate(StaffRequiredMixin, SetHeadlineMixin, UpdateView):
    model = models.ContractType
    fields = '__all__'
    headline = 'Editar tipo de contrato %s'
    template_name = 'core/contract_type_form.html'
    
    def get_headline(self):
        return self.headline % self.get_object()

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('contract_type_list'))


class ContractTypeDelete(StaffRequiredMixin, SetHeadlineMixin, DeleteView):
    model = models.ContractType
    headline = 'Eliminar tipo de contrato %s'
    template_name = 'core/contract_type_delete.html'

    def get_headline(self):
        return self.headline % self.get_object()

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('contract_type_list'))