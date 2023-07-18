from django.contrib import admin
from .models import Marca, Produtos
# Register your models here.
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display=('nome','marca','preco','img',)