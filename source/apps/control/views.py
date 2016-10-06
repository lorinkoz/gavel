# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta

from django.db.models import Q
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone

from braces.views import SetHeadlineMixin

from . import models, forms
from common.mixins import ConsultorRequiredMixin, StaffRequiredMixin


class ContractList(StaffRequiredMixin, SetHeadlineMixin, ListView):
    model = models.Contract
    paginate_by = 25
    page_kwarg = 'p'
    headline = 'Contratos'
    template_name = 'control/contract_list.html'

    def get_queryset(self):
        queryset = super(ContractList, self).get_queryset()
        query = self.request.GET.get('q','')
        if query:
            queryset = queryset.filter(
                Q(uid__iexact=query)|
                Q(entity__name__icontains=query)|
                Q(contract_type__name__icontains=query)|
                Q(payment_type__icontains=query)
            )
        return queryset


class AgedContractList(ContractList):
    headline = 'Contratos próximos a vencerse'

    def get_queryset(self):
        queryset = super(AgedContractList, self).get_queryset()
        return models.Contract.get_aged(queryset)


class TerminatedContractList(ContractList):
    queryset = models.Contract.get_terminated()
    headline = 'Contratos vencidos'


class ContractCreate(StaffRequiredMixin, SetHeadlineMixin, CreateView):
    model = models.Contract
    form_class = forms.ContractForm
    headline = 'Nuevo contrato'
    template_name = 'control/contract_form.html'

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('contract_list'))


class ContractUpdate(StaffRequiredMixin, SetHeadlineMixin, UpdateView):
    model = models.Contract
    form_class = forms.ContractForm
    headline = 'Editar contrato %s'
    template_name = 'control/contract_form.html'
    
    def get_headline(self):
        return self.headline % self.get_object()

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('contract_list'))


class ContractDelete(StaffRequiredMixin, SetHeadlineMixin, DeleteView):
    model = models.Contract
    headline = 'Eliminar contrato %s'
    template_name = 'control/contract_delete.html'

    def get_headline(self):
        return self.headline % self.get_object()

    def get_success_url(self):
        return self.request.GET.get('volver', reverse('contract_list'))