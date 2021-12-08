from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'inp px-3','placeholder':'Usuario'}),
            'password': forms.TextInput(attrs={'class': 'inp px-3','placeholder':'Contraseña','type':'password',"maxlength":"5"})
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
            'password': forms.TextInput(attrs={'class': '','type':'password'})
        }


