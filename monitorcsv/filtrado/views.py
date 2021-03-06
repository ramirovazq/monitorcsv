# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from filtrado.forms import BusquedaForm
from filtrado.utils import *
import logging, csv


formatter = logging.Formatter('%(asctime)s %(message)s')
logger = logging.getLogger('filtro_sitio')
hdlr = logging.FileHandler('/tmp/filtro_sitio.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)



def ver_registros(request):
    from datetime import datetime
    db_csv = settings.ARCHIVO_CSV
    registros_filtrados = []

    ##### todos
    registros = []
    with open(db_csv, 'rb') as csvfile:
        archivo = csv.reader(csvfile, delimiter=str(';'))
        
        for row in archivo:
          #  print epoch_to_string(row[0])
            registros.append(row)
    logger.debug("------------ registros")
    logger.debug(len(registros))
    ##### todos


    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            logger.debug("FORMULARIO VALIDADO")
            logger.debug(form.cleaned_data)
#            logger.debug(form.cleaned_data['status'])
            registros_filtrados = list(registros)


            if form.cleaned_data['status']:
                registros_filtrados = [item for item in registros_filtrados if item[1] == form.cleaned_data['status']]                   
          
            if form.cleaned_data['url']:
                registros_filtrados = [item for item in registros_filtrados if item[2] == form.cleaned_data['url']]                   


            if form.cleaned_data['fecha_inicio']:
                logger.debug("ENTRA FECHA INICIO")
                fecha_inicio_epoch = float(form.cleaned_data['fecha_inicio'].strftime('%s'))
                registros_filtrados = [item for item in registros_filtrados if float(item[0]) >= fecha_inicio_epoch]
                logger.debug(len(registros_filtrados))

            if form.cleaned_data['fecha_fin']:
                fecha_fin_epoch = float(form.cleaned_data['fecha_fin'].strftime('%s'))
                registros_filtrados = [item for item in registros_filtrados if float(item[0]) <= fecha_fin_epoch]


        else:
            logger.debug(form.errors)
    else:
        form = BusquedaForm()


    context = {'registros':registros,
               'form': form,
               'registros_filtrados': registros_filtrados,
              }

    return render(request, 'filtrado/registros_ver.html', context)

