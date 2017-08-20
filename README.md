# monitorcsv
Monitor Csv es un aplicativo, que ayuda a monitorear una URL, guardando los datos en un archivo CSV. Se adiciona desde el administrador la URL del sitio a monitorear, y se indica cada cuanto se desea estar monitoreando (en segundos)

# Requerimientos
Los requerimientos del proyecto
- Django==1.11.4
- requests==2.18.4

# Instalacin
#. Create tu virtualenv

#. Instala las dependencies::
    pip install -r requirements.txt

# Configuracion
#. Indica en el settings.py donde esta tu CSV
    ARCHIVO_CSV = '~/git/monitorcsv/monitorcsv/db.csv'

#. Agrega a las INSTALLED_APPS        
- 'monitor',
- 'filtrado',
        
        
#. Configura tu pais en el settings.py
- LANGUAGE_CODE = 'es-MX'
- TIME_ZONE = 'America/Mexico_City'

# Ejecucion
#. 1. Entra al admin y llena la tabla SitioyFrecuencia 
- llena la url y los segundos del sitio a monitorear

#. 2. Ejecuta el comando:
- $ python manage.py monitorea_sitios

#. 3. Url donde se ven los registros del CSV:
- http://127.0.0.1:8000/registros/ver/
- Los valores del filtro de fecha de inicio y fin, se escriben en el siguiente formato dd-mm-YYYY HH:MM:00 
- Por ejemplo 20-08-2017 17:00:00





    
    


