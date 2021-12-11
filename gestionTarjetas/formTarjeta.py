from django import forms
from gestionTarjetas.models import TipoTarjeta,Tarjeta, Lista



tarjetasTipo = TipoTarjeta.objects.all()
tipos=[]

for i in tarjetasTipo:
    tipos.append((i.id, i.tarjeta_tipo))

class TipoForm(forms.Form):
    tipo = forms.CharField(widget=forms.Select(choices=tipos))


class TarjetaForm(forms.ModelForm):
    foto = forms.FileField()
    class Meta:
        model = Tarjeta
        fields = ('titulo','descripcion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'holabb'}),
            'descripcion': forms.TextInput(attrs={'class':'holabb'})
        }

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('titulo',)
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'holabb'})
        }


class ComentarioForm(forms.ModelForm):
    comentario = forms.Textarea()