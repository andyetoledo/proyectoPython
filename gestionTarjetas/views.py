from django.shortcuts import render, redirect

# Create your views here.
from django.http import response, HttpResponse
from gestionTarjetas.models import *


def mostrar_tarjeta(request):
    tarjetas = Tarjeta.objects.all()
    return render(request,"mostrar_tarjeta.html",{"tarjetas":tarjetas})


from gestionTarjetas.formTarjeta import TarjetaForm,TipoForm,TarjetaForm2

def registrar_tarjeta(request):
    FormularioTarjeta2 = TarjetaForm2(request.POST)
    #anterior
    FormularioTipo = TipoForm(request.POST)

    tarjetas = Tarjeta.objects.all()

    if request.method=="POST":
        if FormularioTipo.is_valid() and FormularioTarjeta2.is_valid() :
            titulo = FormularioTarjeta2.cleaned_data.get("titulo","")
            descripcion = FormularioTarjeta2.cleaned_data.get("descripcion","")
            tipo = FormularioTipo.cleaned_data.get("tipo","")
            nuevaTarjeta = Tarjeta((len(tarjetas)+1),titulo,descripcion,tipo)
            nuevaTarjeta.save()
            #return render(request,"exampleView.html")
    else:
        return render(request, "registrar_tarjeta.html", {"formTipo":FormularioTipo,"formTarjeta2": FormularioTarjeta2})


def detalle_tarjeta(request, id):
    tarjeta = Tarjeta.objects.get(id=id)
    return render(request,"detalle_tarjeta.html",{'tarjeta':tarjeta})


def mis_listas(request):
    return render(request,"exampleView.html")

