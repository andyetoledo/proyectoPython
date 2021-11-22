from django.shortcuts import render

# Create your views here.
from django.http import response, HttpResponse
from gestionTarjetas.models import *


def mostrar_tarjeta(request):
    tarjetas = Tarjeta.objects.all()
    return render(request,"mostrar_tarjeta.html",{"tarjetas":tarjetas})


from gestionTarjetas.formTarjeta import TarjetaForm,TipoForm

def registrar_tarjeta(request):
    FormularioTarjeta = TarjetaForm(request.POST)
    FormularioTipo = TipoForm(request.POST)

    tarjetas = Tarjeta.objects.all()
    if request.method=="POST":
        if FormularioTarjeta.is_valid() and FormularioTipo.is_valid():
            titulo = FormularioTarjeta.cleaned_data.get("titulo","")
            descripcion = FormularioTarjeta.cleaned_data.get("descripcion","")
            tipo = FormularioTipo.cleaned_data.get("tipo","")
            nuevaTarjeta = Tarjeta((len(tarjetas)+1),titulo,descripcion,tipo)

            nuevaTarjeta.save()

            return render(request,"exampleView.html")
    else:
        return render(request, "registrar_tarjeta.html", {"formTarjeta": FormularioTarjeta,"formTipo":FormularioTipo})


def detalle_tarjeta(request):
    return render(request,"exampleView.html")

def mis_listas(request):
    return render(request,"exampleView.html")

