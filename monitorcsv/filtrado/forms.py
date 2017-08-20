# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from filtrado.models import Busqueda

from django.conf import settings #import DATE_INPUT_FORMATS, DATETIME_INPUT_FORMATS

DATETIME_INPUT_FORMATS = ['%d-%m-%Y %H:%M:%S',    # 20-09-2017 17:00:00
 '%d-%m-%Y %H:%M',       # '2006-10-25 14:30'
# '%Y-%m-%d',             # '2006-10-25'
]

class BusquedaForm(forms.Form):

    fecha_inicio = forms.DateTimeField(label="Fecha de inicio", required=False, input_formats=DATETIME_INPUT_FORMATS)
    fecha_fin = forms.DateTimeField(label="Fecha de fin", required=False, input_formats=DATETIME_INPUT_FORMATS)
    status = forms.CharField(label="Status", required=False,)
    url = forms.CharField(label="URL", required=False,)


    #class Meta:
     #   model = Busqueda
      #  fields = ['fecha_inicio', 'fecha_fin', 'status','url']
