# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
import requests, logging, csv
import time


@python_2_unicode_compatible
class Busqueda(models.Model):
    fecha_inicio = models.DateTimeField(blank=True, null=True)#
    fecha_fin = models.DateTimeField(blank=True, null=True)#
    status = models.CharField(max_length=250, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return u"%s" % (self.id)

