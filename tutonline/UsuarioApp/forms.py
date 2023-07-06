from django import forms
from api.models import *
from django.contrib.admin import widgets
from django.core import validators 
from django.forms import ValidationError
from api.models import Profesion

class FormProfesion(forms.ModelForm):
    anioEgreso = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        label="Año de Egreso"
    )
    class Meta:
        model = Profesion
        fields = [
            'codigoVerificador',
            'institucion',
            'profesion',
            'anioEgreso',
        ]

        labels = {
            'codigoVerificador' : 'Código Verificador',
            'institucion' : 'Institución',
            'profesion' : 'Profesión'
        }