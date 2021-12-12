import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count,Sum
from django.shortcuts import render, redirect

# Create your views here.
from django.http import response, HttpResponse
from gestionTarjetas.models import *
from gestionTarjetas.formTarjeta import *


def mostrar_tarjeta(request):

    if request.method=="POST":
        if request.POST.get('nombreTarjeta') is not None:
            tarjetas=Tarjeta.objects.filter(titulo=request.POST.get('nombreTarjeta'))

            if tarjetas is None:
                msg = 'no hay tarjetas'
                return render(request, 'mostrar_tarjeta.html', {"Error": msg})

            return render(request,'mostrar_tarjeta.html',{"tarjetas":tarjetas})



    FormularioTipo = TipoForm(request.POST)
    if request.method == "POST":
        if FormularioTipo.is_valid():
            tipoSelect = FormularioTipo.cleaned_data.get("tipo", "value")
            tipo = TipoTarjeta.objects.get(tipo=tipoSelect)
            tarjetas = Tarjeta.objects.filter(idtipotarjeta=tipo.id)
            return render(request, 'mostrar_tarjeta.html', {"tarjetas": tarjetas})

    tarjetas = Tarjeta.objects.all()
    return render(request,"mostrar_tarjeta.html",{"tarjetas":tarjetas,'buscartipo':FormularioTipo})

def registrar_tarjeta(request):
    FormularioTarjeta2 = TarjetaForm(request.POST, request.FILES)
    FormularioTipo = TipoForm(request.POST)

    if request.method=="POST":
        tarjetas = Tarjeta.objects.all()
        publicacion = Publicacion.objects.all()
        if FormularioTipo.is_valid() and FormularioTarjeta2.is_valid():
            titulo = FormularioTarjeta2.cleaned_data.get("titulo", "")
            descripcion = FormularioTarjeta2.cleaned_data.get("descripcion", "")
            tipo = FormularioTipo.cleaned_data.get("tipo", "")
            foto = request.FILES.get("foto")

            nuevaTarjeta = Tarjeta((len(tarjetas)+1), titulo, descripcion, foto, tipo)
            publicacionTarjeta = Publicacion((len(publicacion)+1),datetime.date.today(),len(tarjetas),request.user.id)

            nuevaTarjeta.save()
            publicacionTarjeta.save()
            return render(request,"mostrar_tarjeta.html")
    else:
        return render(request, "registrar_tarjeta.html", {"formTipo":FormularioTipo,"formTarjeta": FormularioTarjeta2})


def detalle_tarjeta(request, id):
    tarjeta = Tarjeta.objects.get(id=id)
    publicacion = Publicacion.objects.get(idtarjeta=id)

    #print(califSuma)
    if request.method=="POST":
        Like = request.POST.get('Like')
        Dislike = request.POST.get('Dislike')
        try:
            validarVoto = Califiacion.objects.get(idtarjeta=id,idusuario=request.user.id)
        except ObjectDoesNotExist:
            validarVoto = None
        if validarVoto is None:
            if Like is not None:
                califId = Califiacion.objects.all()
                calificacion = Califiacion((len(califId)+1),1,id,request.user.id)
                calificacion.save()
            elif Dislike is not None:
                califId = Califiacion.objects.all()
                calificacion = Califiacion((len(califId)+1), -1, id, request.user.id)
                calificacion.save()
        else:
            if Like is not None:
                validarVoto.putucion = 1
                validarVoto.save()
            elif Dislike is not None:
                validarVoto.putucion = -1
                validarVoto.save()
    califSuma = Califiacion.objects.filter(idtarjeta=id).aggregate(Sum('putucion'))
    print(califSuma)
    if califSuma['putucion__sum'] is None:
        califSuma['putucion__sum'] = 0




    return render(request,"detalle_tarjeta.html",{'tarjeta':tarjeta,'publicacion':publicacion,'puntos':califSuma})


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


