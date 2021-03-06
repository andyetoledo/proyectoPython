import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import render


from gestionTarjetas.formTarjeta import *


def mostrar_tarjeta(request):
    FormularioTipo = TipoForm(request.POST)
    if request.method=="POST":
        if request.POST.get('nombreTarjeta') !="":
            tarjetas=Tarjeta.objects.filter(titulo=request.POST.get('nombreTarjeta'))
            if tarjetas is None:
                msg = 'no hay tarjetas'
                return render(request, 'mostrar_tarjeta.html', {"Error": msg})
            return render(request,'mostrar_tarjeta.html',{"tarjetas":tarjetas,'buscartipo':FormularioTipo['tipo']})
    if request.method == "POST":
        if FormularioTipo.is_valid():
            idtipo = FormularioTipo.cleaned_data.get("tipo", "")
            tarjetas = Tarjeta.objects.filter(idtipotarjeta=idtipo)
            return render(request, 'mostrar_tarjeta.html', {"tarjetas": tarjetas,'buscartipo':FormularioTipo['tipo']})
    tarjetas = Tarjeta.objects.all()
    return render(request,"mostrar_tarjeta.html",{"tarjetas":tarjetas,'buscartipo':FormularioTipo['tipo']})

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
            print(tipo!="0")
            if tipo!="0":
                foto = request.FILES.get("foto")
                nuevaTarjeta = Tarjeta((len(tarjetas)+1), titulo, descripcion, foto, tipo)
                publicacionTarjeta = Publicacion((len(publicacion)+1),datetime.date.today(),len(tarjetas)+1,request.user.id)
                nuevaTarjeta.save()
                publicacionTarjeta.save()
                tarjetas = Tarjeta.objects.all()
                return render(request,"mostrar_tarjeta.html",{'tarjetas':tarjetas})
            return render(request, "registrar_tarjeta.html",{"formTipo": FormularioTipo, "formTarjeta": FormularioTarjeta2})
    else:
        return render(request, "registrar_tarjeta.html", {"formTipo":FormularioTipo,"formTarjeta": FormularioTarjeta2})


def detalle_tarjeta(request, id):
    tarjeta = Tarjeta.objects.get(id=id)
    publicacion = Publicacion.objects.get(idtarjeta=id)
    comentarioForm = ComentarioForm(request.POST)
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
    if califSuma['putucion__sum'] is None:
        califSuma['putucion__sum'] = 0
    if request.method == "POST":
        if comentarioForm.is_valid():
            nuevoComentario = comentarioForm.cleaned_data.get('comentario')
            idcomentario = Comentarios.objects.all()
            Coment = Comentarios(len(idcomentario)+1,nuevoComentario,id,request.user.id)
            Coment.save()
            comentarioForm = ComentarioForm()
    comentariosTarjeta = Comentarios.objects.filter(idtarjeta=id)
    listasUsuario = Lista.objects.filter(idusuario=request.user.id)

    if request.method=='POST':
        agregarTarjetaLista = request.POST.get('dropdown')
        if agregarTarjetaLista!="":
            lista = Lista.objects.get(idusuario=request.user.id,id=agregarTarjetaLista)
            tarjeta.lista_set.add(lista.id)
    return render(request,"detalle_tarjeta.html",{'tarjeta':tarjeta,'publicacion':publicacion,'puntos':califSuma,'comentarioForm':comentarioForm,'comentario':comentariosTarjeta,'listas':listasUsuario})


def mis_listas(request):
    tarjetas = ''
    FormularioLista = ListaForm(request.POST)
    if request.method == "POST":
        if FormularioLista.is_valid():
             listas = Lista.objects.all()
             titulo = FormularioLista.cleaned_data.get("titulo","")
             nuevaLista = Lista((len(listas)+1), titulo,request.user.id)
             nuevaLista.save()
             FormularioLista = ListaForm(request.POST)

    if request.method == "POST":
        idlista = request.POST.get('dropdown')
        if idlista is not None:
            lista = Lista.objects.get(id=idlista)
            tarjetas = lista.tarjeta_lista.filter(lista=lista)
    listasUsuario = Lista.objects.filter(idusuario=request.user.id)
    return render(request, "crearLista.html", {"FormularioLista":FormularioLista,'listas':listasUsuario,'tarjetas':tarjetas})


