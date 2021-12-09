from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'inp px-3','placeholder':'Usuario'}),
            'password': forms.TextInput(attrs={'class': 'inp px-3','type':'password','placeholder':'Contraseña'})
        }

class Registro(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': ''}),
            'first_name': forms.TextInput(attrs={'class': ''}),
            'last_name': forms.TextInput(attrs={'class': ''}),
            'email': forms.TextInput(attrs={'class': ''}),
            'password': forms.PasswordInput(attrs={'class': ''}),
        }

class RegistroUsuario(UserCreationForm):
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