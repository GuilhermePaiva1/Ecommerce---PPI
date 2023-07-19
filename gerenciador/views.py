from gc import get_objects
from django.shortcuts import render
from .models import Marca, Produtos
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    produtos = Produtos.objects.all()
    context = {'produtos': produtos}
    return render(request, 'pags/index.html', context)

def detalhe_produto(request, id_produto):
    produto = get_object_or_404(Produtos, id=id_produto)

    context = {'produto': produto}
    return render(request, 'pags/detalhe_produto.html', context)

def dashboard(request):
    total_produtos = Produtos.objects.count()
    total_marca = Marca.objects.count()
    context = {
        'total_produtos' : total_produtos,
        'total_marca' : total_marca,
    }
    return render(request, "Administrador/dashboard.html",context)

def listar_produtos(request):
    produtos = Produtos.objects.all()
    context = {'produtos': produtos}

    return render(request, 'Administrador/Produtos.html', context)