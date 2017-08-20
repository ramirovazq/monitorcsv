# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from filtrado.forms import BusquedaForm
import logging, csv


formatter = logging.Formatter('%(asctime)s %(message)s')
logger = logging.getLogger('filtro_sitio')
hdlr = logging.FileHandler('/tmp/filtro_sitio.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)



def ver_registros(request):
    db_csv = settings.ARCHIVO_CSV

    ##### todos
    registros = []
    with open(db_csv, 'rb') as csvfile:
        archivo = csv.reader(csvfile, delimiter=str(';'))
        
        for row in archivo:
            registros.append(row)
    ##### todos


    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            logger.debug("FORMULARIO VALIDADO")
            logger.debug(form.cleaned_data)
            logger.debug(form.cleaned_data['status'])
            registros_filtrados = []

            for item in registros:
                print item
                if item[1] == form.cleaned_data['status'] or item[2] == form.cleaned_data['url']:
                    registros_filtrados.append(item)
            print registros_filtrados

        else:
            logger.debug(form.errors)
    else:
        registros_filtrados = []
        form = BusquedaForm()

    context = {'registros':registros,
               'form': form,
               'registros_filtrados': registros_filtrados,
              }

    return render(request, 'filtrado/registros_ver.html', context)

