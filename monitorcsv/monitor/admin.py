# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from monitor.models import SitioyFrecuencia

# Register your models here.

class SitioyFrecuenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'frecuencia_segundos']


admin.site.register(SitioyFrecuencia, SitioyFrecuenciaAdmin)

