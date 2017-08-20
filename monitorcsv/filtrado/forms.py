# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from filtrado.models import Busqueda

from django.conf import settings #import DATE_INPUT_FORMATS, DATETIME_INPUT_FORMATS

DATETIME_INPUT_FORMATS = ['%d-%m-%Y %H:%M:%S',    # '2006-10-25 14:30:59'
 '%d-%m-%Y %H:%M',       # '2006-10-25 14:30'
 '%Y-%m-%d',             # '2006-10-25'
]

class BusquedaForm(ModelForm):

    class Meta:
        model = Busqueda
        fields = ['fecha_inicio', 'fecha_fin', 'status']
