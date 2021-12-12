from django import forms
from gestionTarjetas.models import TipoTarjeta,Tarjeta, Lista



tarjetasTipo = TipoTarjeta.objects.all()
tipos=[]

for i in tarjetasTipo:
    tipos.append((i.id, i.tarjeta_tipo))

class TipoForm(forms.Form):
    tipo = forms.CharField(widget=forms.Select(choices=tipos,attrs={'class':'form-controlDrop'}))







class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ('titulo','descripcion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }



class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('titulo',)
        widgets = {
            'titulo': forms.TextInput(attrs={'class':''})
        }


class ComentarioForm(forms.ModelForm):
    comentario = forms.Textarea()