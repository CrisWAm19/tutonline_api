from django import forms
from api.models import *
from django.contrib.admin import widgets
from django.core import validators 
from django.forms import ValidationError

class FormPublicacion(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = '__all__'