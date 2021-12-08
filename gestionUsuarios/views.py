from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from .formUsuario import Registro

from gestionUsuarios.models import TipoUsuario
from django.contrib.auth.models import User

from django.contrib.auth import logout,authenticate
from gestionUsuarios.formUsuario import Login

def registrar_usuario(request):
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

    context = {'formRegistro': formRegistro}
    return render(request, "registrar_usuario.html", context)

def editar_usuario(request):
    return render(request,"exampleView.html")

def base_wiki(request):
    b = get_template('baseWiki.html')
    return HttpResponse(b.render({}))

#Para los errores
def error_404(request,exception): #pagina no encontrada
    return render(request, "error404.html")

def error_500(request): #Error en el server
    return render(request, "error500.html")

def error_403(request,exception): #Permiso denegado
    return render(request, "error403.html")

def error_400(request,exception): #Solicitud incorrecta
    return render(request, "error400.html")

def iniciar_sesion(request):
    loginForm = Login(request.POST)
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                Login(request, user)
                print("a")
                return render(request,'mostrar_tarjeta.html')
            else:
                print("b")
                return redirect('login')
    return render(request, "login.html", {'loginForm':loginForm})

def prueba(request):
    b = get_template('prueba.html')
    return HttpResponse(b.render({}))