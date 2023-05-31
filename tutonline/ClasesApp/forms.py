from django import forms
from api.models import *
from django.contrib.admin import widgets
from django.core import validators 
from django.forms import ValidationError

class FormClase(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        label="Fecha de la clase"
    )
    hora = forms.TimeField(
        widget= forms.TimeInput(attrs = {'type':'time'}),
        label="Hora de la clase"
    )
    modalidad = forms.ChoiceField(
        choices=(
            ('Presencial', 'Presencial'),
            ('Online', 'Online'),
        ),
        label="Modalidad"
    )

    class Meta:
        model = Clase
        # fields = '__all__'
        fields = [
            'fecha',
            'hora',
            'modalidad',
            'tarifa',
            'idAsignatura',
        ]
        labels = {
            'tarifa':'Tarifa',
            'idAsignatura':'Asignatura'
        }

class FormClaseAgendada(forms.ModelForm):
    idEstudiante = forms.ModelChoiceField(
        queryset=User.objects.filter(tipoDeUsuario='Estudiante'),
        label='Estudiante',
        to_field_name='rut',
    )

    class Meta:
        model = ClaseAgendada
        fields = [
            'idClase',
            'idEstudiante'
        ]
        labels = {
            'idClase': 'Clase',
            'idEstudiante': 'Estudiante'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idEstudiante'].queryset = User.objects.filter(tipoDeUsuario='Estudiante')
        
    def label_from_instance(self, obj):
        return obj.rut