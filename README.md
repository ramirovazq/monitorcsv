# monitorcsv
Monitor Csv es un aplicativo, que ayuda a monitorear una URL, guardando los datos en un archivo CSV. Se adiciona desde el administrador la URL del sitio a monitorear, y se indica cada cuanto se desea estar monitoreando (en segundos)

Los requerimientos del proyecto
- Django==1.11.4
- requests==2.18.4

#. Create tu virtualenv

#. Instala las dependencies::
    pip install -r requirements.txt

#. Indica en el settings donde esta tu CSV
    ARCHIVO_CSV = '~/git/monitorcsv/monitorcsv/db.csv'

#. Agrega a las INSTALLED_APPS
        ...
        'monitor',
        'filtrado',
        ...
        
#. Configura tu pais        
LANGUAGE_CODE = 'es-MX'
TIME_ZONE = 'America/Mexico_City'



    
    


