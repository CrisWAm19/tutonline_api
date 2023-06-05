from django import forms
from api.models import *
from django.contrib.admin import widgets
from django.core import validators 
from django.forms import ValidationError

class FormPublicacion(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = [
            'titulo',
            'descripcionPublicacion',
            'idAsignatura'
        ]
        labels = {
            'titulo' : 'Título',
            'descripcionPublicacion' : 'Descripción',
            'idAsignatura' : 'Asignatura (opcional)'
        }