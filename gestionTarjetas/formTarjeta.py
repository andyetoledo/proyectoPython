from django import forms
from gestionTarjetas.models import TipoTarjeta
tarjetasTipo = TipoTarjeta.objects.all()
tipos=[]


for i in tarjetasTipo:
    tipos.append((i.id, i.tarjeta_tipo))

class TipoForm(forms.Form):
    tipo = forms.CharField(widget=forms.Select(choices=tipos))

class TarjetaForm(forms.Form):
     titulo = forms.CharField(max_length=25)
     descripcion = forms.CharField(max_length=350)
     # foto = models.ImageField()

