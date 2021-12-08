from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.

from gestionUsuarios.models import TipoUsuario
from django.contrib.auth.models import User

def iniciar_sesion(request):
    return render(request,"exampleView.html")

def registrar_usaurio(request):
    return render(request,"exampleView.html")

def editar_usaurio(request):
    return render(request,"exampleView.html")

def base_wiki(request):
    b = get_template('baseWiki.html')
    return HttpResponse(b.render({}))

#Para los errores
def error404(request): #pagina no encontrada
    return render(request,"exampleView.html")

def error500(request): #Error en el server
    return render(request,"exampleView.html")

def error403(request): #Permiso denegado
    return render(request,"exampleView.html")

def error400(request): #Solicitud incorrecta
    return render(request,"exampleView.html")

