# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
import csv

def ver_registros(request):
    db_csv = settings.ARCHIVO_CSV

    registros = []
    with open(db_csv, 'rb') as csvfile:
        archivo = csv.reader(csvfile, delimiter=str(';'))
        
        for row in archivo:
            registros.append(row)

    context = {'registros':registros}

    return render(request, 'filtrado/registros_ver.html', context)

