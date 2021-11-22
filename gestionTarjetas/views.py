from django.shortcuts import render

# Create your views here.

from gestionTarjetas.models import *


def mostrar_tarjeta(request):
    tarjetas = Tarjeta.objects.all()
    return render(request,"mostrar_tarjeta.html",{"tarjetas":tarjetas})

def registrar_tarjeta(request):
    return render(request,"exampleView.html")

def detalle_tarjeta(request):
    return render(request,"exampleView.html")

def mis_listas(request):
    return render(request,"exampleView.html")

