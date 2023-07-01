from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from api.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


Usuario = get_user_model()
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
    

class FormActualizarPerfil(UserChangeForm):
    fechaNacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        label="Fecha de Nacimiento"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'fechaNacimiento', 'numeroTelefono', 'region', 'comuna', 'email']
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'fechaNacimiento':'Fecha de nacimiento',
            'numeroTelefono':'Teléfono',
            'region':'Región',
            'comuna':'Comuna',
            'email':'Correo electrónico',
        }