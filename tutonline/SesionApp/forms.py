from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from api.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from itertools import cycle

Usuario = get_user_model()
def validate_numero_telefono(value):
    if value < 0:
        raise ValidationError("El número de teléfono no puede ser negativo.")
    if len(str(value)) != 9:
        raise ValidationError("El número de teléfono debe tener 9 dígitos.")



def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")
    rut_digits, verification_digit = rut[:-1], rut[-1]
    
    # Validar que el rut tenga solo dígitos y el dígito verificador sea un dígito o "k" (para caso de rut con dígito verificador 10)
    if not rut_digits.isdigit() or (verification_digit != "k" and not verification_digit.isdigit()):
        raise ValidationError("El RUT debe contener solo dígitos y el dígito verificador debe ser un dígito numérico o la letra 'k'.")
    
    # Calcular el dígito verificador esperado
    reverse_digits = rut_digits[::-1]
    factors = cycle(range(2, 8))
    checksum = sum(int(digit) * factor for digit, factor in zip(reverse_digits, factors))
    expected_verification_digit = str((11 - (checksum % 11)) % 11)
    if expected_verification_digit == "10":
        expected_verification_digit = "k"
    
    # Comparar el dígito verificador esperado con el dígito verificador del rut
    if expected_verification_digit != verification_digit:
        raise ValidationError("El RUT ingresado no es válido.")
    
    return True


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        help_text="Máximo 150 caracteres. Solo se permiten letras, dígitos y @/./+/-/_.",
    )

    numeroTelefono = forms.IntegerField(
        label="Teléfono",
        validators=[validate_numero_telefono]
    )
    rut = forms.CharField(
        label="Rut",
        validators=[validar_rut]
    )

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
            'rut':'Rut',
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
    numeroTelefono = forms.IntegerField(
        label="Teléfono",
        validators=[validate_numero_telefono]
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