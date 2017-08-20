from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ver/$', views.ver_registros, name="ver_registros"),    
]

