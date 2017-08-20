# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from filtrado.models import Busqueda

from django.conf import settings #import DATE_INPUT_FORMATS, DATETIME_INPUT_FORMATS

DATETIME_INPUT_FORMATS = ['%d-%m-%Y %H:%M:%S',    # '2006-10-25 14:30:59'
 '%d-%m-%Y %H:%M',       # '2006-10-25 14:30'
 '%Y-%m-%d',             # '2006-10-25'
]

class BusquedaForm(forms.Form):

    fecha_inicio = forms.CharField(label="Fecha de inicio", required=False,)
    fecha_fin = forms.CharField(label="Fecha de inicio", required=False,)
    status = forms.CharField(label="Status", required=False,)
    url = forms.CharField(label="URL", required=False,)


    #class Meta:
     #   model = Busqueda
      #  fields = ['fecha_inicio', 'fecha_fin', 'status','url']
