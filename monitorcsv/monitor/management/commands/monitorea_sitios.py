## coding: UTF-8
from django.core.management.base import BaseCommand
from monitor.models import SitioyFrecuencia


class Command(BaseCommand):

    def handle(self, *args, **options):
        import time
        
        while True:
            for sitio in SitioyFrecuencia.objects.all():
                sitio.checar()
                time.sleep(sitio.frecuencia_segundos)
