from django.shortcuts import render, redirect

# Create your views here.
from django.http import response, HttpResponse
from gestionTarjetas.models import *
from gestionTarjetas.formTarjeta import *


def mostrar_tarjeta(request):
    #aqui chambeado porque no me pagan y solo quiero pasar la materia :3
    #if request.method=="GET":
    #    Tarjeta.objects.filter(titulo=request.GET('nombreTarjeta'))

    tarjetas = Tarjeta.objects.all()
    return render(request,"mostrar_tarjeta.html",{"tarjetas":tarjetas})

def registrar_tarjeta(request):
    FormularioTarjeta2 = TarjetaForm(request.POST, request.FILES)
    FormularioTipo = TipoForm(request.POST)
    tarjetas = Tarjeta.objects.all()
    if request.method=="POST":
        if FormularioTipo.is_valid() and FormularioTarjeta2.is_valid():
            titulo = FormularioTarjeta2.cleaned_data.get("titulo", "")
            descripcion = FormularioTarjeta2.cleaned_data.get("descripcion", "")
            tipo = FormularioTipo.cleaned_data.get("tipo", "")
            foto = request.FILES.get("foto")
            nuevaTarjeta = Tarjeta((len(tarjetas)+1), titulo, descripcion, foto, tipo)
            nuevaTarjeta.save()
            return render(request,"exampleView.html")
    else:
        return render(request, "registrar_tarjeta.html", {"formTipo":FormularioTipo,"formTarjeta2": FormularioTarjeta2})


def detalle_tarjeta(request, id):
    tarjeta = Tarjeta.objects.get(id=id)

    return render(request,"detalle_tarjeta.html",{'tarjeta':tarjeta})


def mis_listas(request):
    FormularioLista = ListaForm(request.POST)
    if request.method == "POST":
        if FormularioLista.is_valid():
             listas = Lista.objects.all()
             titulo = FormularioLista.cleaned_data.get("titulo","")
             nuevaLista = Lista((len(listas)+1), titulo)
             nuevaLista.save()
             FormularioLista = ListaForm(request.POST)
    return render(request, "crearLista.html", {"FormularioLista":FormularioLista})


