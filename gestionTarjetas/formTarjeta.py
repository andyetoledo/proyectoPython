from django import forms
from gestionTarjetas.models import TipoTarjeta,Tarjeta



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


class TarjetaForm2(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ('titulo','descripcion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'holabb'}),
            'descripcion': forms.TextInput(attrs={'class':'holabb'})
        }

