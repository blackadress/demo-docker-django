from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, label='Nombres')
    last_name = forms.CharField(max_length=50, required=True, label='Apellidos')
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserLogin(forms.Form):
    username = forms.CharField(max_length=40, required=True, label="Nombre de usuario")
    password = forms.CharField(max_length=40, required=True, label='Contraseña', widget=forms.PasswordInput())
