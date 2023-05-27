from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from api.models import User
# User = get_user_model()

# from 
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2','tipoDeUsuario']
        # labels = {
        #     'username':'',
        #     'first_name':'',
        #     'last_name':'',
        #     'email':'',
        #     'password1':'',
        #     'password2':''
        # }