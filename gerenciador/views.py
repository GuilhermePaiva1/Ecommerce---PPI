from gc import get_objects
from django.shortcuts import render
from .models import Marca, Produtos
from django.shortcuts import get_object_or_404, redirect
from .forms import MarcaForm, ProdutoForm
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

def listar_marcas(request):
    marca = Marca.objects.all()
    context = {'marcas': marca}

    return render(request, 'Administrador/Marcas.html', context)

def criar_marca(request):
    if request.method == "POST":

        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = MarcaForm()
            return redirect('listar_marcas')

    else: 
        form = MarcaForm()

    return render(request, 'forms/forms_marcas.html', {'form': form})

def produto_editar(request,id):
    produto = get_object_or_404(Produtos,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST,request.FILES,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request,'forms/forms_produtos.html',{'form':form})

def produto_remover(request, id):
    produto = get_object_or_404(Produtos, id=id)
    produto.delete()
    return redirect('listar_produtos')

def listar_marcas(request):
    marcas = Marca.objects.all()
    context = {'marcas': marcas}

    return render(request,'Administrador/Marcas.html', context)

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()

    return render(request, "forms/forms_produtos.html", {'form': form})

def marca_editar(request, id):
    marca = get_object_or_404(Marca, id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else: 
        form = MarcaForm(instance=marca)
    
    return render(request, 'forms/forms_marcas.html', {'form': form})

def marca_remover(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    return redirect('listar_marcas')



