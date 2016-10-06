# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from . import models


class ContractForm(forms.ModelForm):
    
    class Meta:
        model = models.Contract
        fields = ('uid', 'entity', 'contract_type', 'date_signed', 'date_termination', 'payment_type', 'notes')
