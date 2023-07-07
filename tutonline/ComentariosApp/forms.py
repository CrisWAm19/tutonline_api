from django import forms
from api.models import *
from django.core.exceptions import ValidationError

def validate_valoracion(value):
    if value < 1 or value > 5:
        raise ValidationError("La valoración debe estar entre 1 y 5")
    
class FormComentario(forms.ModelForm):

    valoracion = forms.IntegerField(
        label="Valorar del 1 al 5",
        validators=[validate_valoracion]
    )
    class Meta:
        model = Comentario
        fields = [
            'comentario',
            'valoracion',
        ]