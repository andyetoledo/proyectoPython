from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

# Create your views here.
from django.urls import reverse_lazy

from .formUsuario import RegistroUsuario, EditarPerfil, contraseñaForm,RegistroTipoUsuario

from gestionUsuarios.models import TipoUsuario
from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth import login, logout, authenticate
from gestionUsuarios.formUsuario import Login

"""
def registrar_usuario2(request):
    formRegistro = Registro(request.POST)
    if request.method == "POST":
        if formRegistro.is_valid():
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            USER = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            USER.save()
            return redirect('login')
    context = {'formRegistro': formRegistro}
    return render(request, "registrar_usuario.html", context)
"""

def registrar_usuario(request):
    formRegistro = RegistroUsuario(request.POST)
    formRegistroTipo = RegistroTipoUsuario(request.POST)
    if request.method == "POST":
        if formRegistro.is_valid() and formRegistroTipo.is_valid():
            formRegistro.save()
            username = User.objects.last()
            user = User.objects.get(username=username)
            idtipo = formRegistroTipo.cleaned_data.get("tipo", "")
            print(user.id,idtipo)
            user.tipousuario_set.add(idtipo,user.id)
            return redirect('login')
    context = {'formRegistro': formRegistro,'formRegistroTipoUsuario':formRegistroTipo}
    return render(request, "registrar_usuario.html", context)

def editar_usuario(request):
    usuario = User.objects.get(id=request.user.id)
    formEditar = EditarPerfil(instance=usuario)
    if request.method == "POST":
        formEditar = EditarPerfil(request.POST, instance=usuario)
        if formEditar.is_valid():
            formEditar.save()
            return redirect('mostrarTarjeta')
    context = {'formEditar': formEditar}
    return render(request, "editar_usuario.html", context)


def base_wiki(request):
    b = get_template('baseWiki.html')
    return HttpResponse(b.render({}))

#Para los errores
def error404(request, exception):
    return render(request,'error404.html')

def error403(request, exception):
    return render(request,'error403.html')

def error400(request, exception):
    return render(request,'error400.html')

def error500(request):
    return render(request,'error500.html')


def iniciar_sesion(request):

    loginForm = Login(request.POST)
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mostrarTarjeta')
            else:
                mensaje = "Usuario o contraseña incorrecta"
                return render(request, "login.html", {'loginForm': loginForm,'msg':mensaje})
    return render(request, "login.html", {'loginForm':loginForm})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def prueba(request):
    b = get_template('prueba.html')
    return HttpResponse(b.render({}))

def cambio_contraseña(PasswordChangeView):
    template_name = 'templates/cambio_contraseña.html'
    success_url = reverse_lazy('editarU')
