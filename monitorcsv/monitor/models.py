# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
import requests, logging, csv
import time

# Logging

formatter = logging.Formatter('%(asctime)s %(message)s')
logger = logging.getLogger('check_sitio')
hdlr = logging.FileHandler('/tmp/check_sitio.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)



@python_2_unicode_compatible
class SitioyFrecuencia(models.Model):
    url = models.URLField(blank=True, null=True)
    frecuencia_segundos = models.IntegerField(default=5)
    wait_segundos = models.IntegerField(default=6)#tiempo de espera de la respuesta


    def checar(self):
        db_csv = settings.ARCHIVO_CSV
        
        with open(db_csv, 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=str(u';'), quoting=csv.QUOTE_MINIMAL)
            timestamp = int(time.time())
            try:
                response = requests.get(self.url, timeout=self.wait_segundos)
                logger.debug(u"%s" % response.status_code)
                if response.status_code == 200:
                    spamwriter.writerow([timestamp,'UP','%s' % self.url])
                else:
                    spamwriter.writerow([timestamp,'DOWN' ,'%s' % self.url])
            except requests.exceptions.Timeout:
                spamwriter.writerow([timestamp,'DOWN' ,'%s' % self.url])
                logger.debug("DOWN")
            except requests.exceptions.ConnectionError:
                spamwriter.writerow([timestamp,'DOWN' ,'%s' % self.url])
                logger.debug("DOWN")
            except Exception as e:
                spamwriter.writerow([timestamp,'?' ,'%s' % self.url])
                error_corto = str(e)[:10]
                logger.debug(error_corto)
        return None

    def __str__(self):
        return u"%s, (frecuencia %s segundos)" % (self.url, self.frecuencia_segundos)


