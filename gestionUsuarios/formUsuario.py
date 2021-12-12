from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from gestionUsuarios.models import TipoUsuario

class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'inp px-3','placeholder':'Usuario'}),
            'password': forms.TextInput(attrs={'class': 'inp px-3','type':'password','placeholder':'Contraseña'})
        }




tarjetasTipo = TipoUsuario.objects.all()
tipos=[]

for i in tarjetasTipo:
    tipos.append((i.id, i.usuario_tipo))

class RegistroTipoUsuario(forms.Form):
    tipo = forms.CharField(widget=forms.Select(choices=tipos, attrs={'class': 'form-control me-3'}))








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
    '''password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),
    )'''
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class contraseñaForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}))

    class Meta:
        model = User
        fields = ( 'old_password','new_password1','new_password2')
