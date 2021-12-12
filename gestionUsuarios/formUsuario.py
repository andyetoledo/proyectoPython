from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'inp px-3','placeholder':'Usuario'}),
            'password': forms.TextInput(attrs={'class': 'inp px-3','type':'password','placeholder':'Contraseña'})
        }


class RegistroUsuario(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control','placeholder':'Ingresa tu contraseña'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control','placeholder':'**********'}),
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tus nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tus apellidos'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa tu correo electrónico'}),
        }

class EditarPerfil(UserChangeForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }