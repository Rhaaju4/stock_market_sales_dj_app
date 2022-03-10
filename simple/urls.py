import imp
from django import views
from django.contrib import admin
from django.urls import path
from py2json_app import views
from natural_language_processing import views as _nlp
from machine_learning import views as _ml
from deep_learning import views as _dl

#from simple.py2json_app.views import json_reading 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dlj/', _dl.str2json),
    path("nlp/", _nlp.natural_language_processing2), 
    path("ml/", _ml.machine_learning2),
    path("dl/", _dl.deep_learning2),
    path("dlsmsp/", _dl.data_vizual),
    ]
