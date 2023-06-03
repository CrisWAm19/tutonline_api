from django import forms
from django.contrib.auth.forms import UserCreationForm
from api.models import User
import json
# comunas_data = {
#     "regiones": [
#         {
#             "region": "Arica y Parinacota",
#             "comunas": ["Arica", "Camarones", "Putre", "General Lagos"]
#         },
#         {
#             "region": "Tarapacá",
#             "comunas": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
#         },
#     ]
    
# }


# from 
class CustomUserCreationForm(UserCreationForm):
    fechaNacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        label="Fecha de Nacimiento"
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput,
    )
    # = forms.ChoiceField(choices=[(region, region) for region in comunas_data.keys()], label='Región')
    # comuna = forms.ChoiceField(choices=[], label='Comuna')
    class Meta:
        model = User
        fields =['username',
                 'rut',
                 'first_name',
                 'last_name',
                 'tipoDeUsuario',
                 'fechaNacimiento',
                 'numeroTelefono',
                 'region',
                 'comuna',
                 'email',
                 'password1',
                 'password2',
                 ]
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'tipoDeUsuario':'Seleccione su rol',
            'fechaNacimiento':'Fecha de nacimiento',
            'numeroTelefono':'Teléfono',
            'region':'Región',
            'comuna':'Comuna',
            'email':'Correo electrónico',
            'password1':'Contraseña',
            'password2':'Confirmar Contraseña',
        }
    