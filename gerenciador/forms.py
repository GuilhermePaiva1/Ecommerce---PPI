from django.forms import ModelForm
from django import forms
from .models import Marca, Produtos

class MarcaForm(ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
        }

class ProdutoForm(ModelForm):

    class Meta:
        model = Produtos
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'marca' : forms.Select(attrs={'class': 'form-control' }),
            'informacoes' : forms.TextInput(attrs={'class': 'form-control' }),
            'preco': forms.TextInput(attrs={'class': 'form-control' }),
            'img': forms.FileInput(attrs={'class': 'form-control' })
        }