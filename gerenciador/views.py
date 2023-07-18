from gc import get_objects
from django.shortcuts import render
from .models import Marca, Produtos
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    produtos = Produtos.objects.all()
    context = {'produtos': produtos}
    return render(request, 'pags/index.html', context)