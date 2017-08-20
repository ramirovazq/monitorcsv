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

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            pass
            #osea se hace filtrado
        else:
            logger.debug(form.errors)
    else:
        form = BusquedaForm()

    registros = []
    with open(db_csv, 'rb') as csvfile:
        archivo = csv.reader(csvfile, delimiter=str(';'))
        
        for row in archivo:
            registros.append(row)


    context = {'registros':registros, 'form': form}

    return render(request, 'filtrado/registros_ver.html', context)

