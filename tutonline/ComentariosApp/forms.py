from django import forms
from api.models import *


class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'comentario',
            'valoracion',
        ]
    