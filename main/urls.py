"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from gerenciador.views import index, detalhe_produto, dashboard, listar_produtos, listar_marcas, criar_produto, produto_editar, produto_remover,listar_marcas, criar_marca, marca_editar, marca_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('detalhe_produto/<int:id_produto>/', detalhe_produto, name='detalhe_produto'),
    path('dashboard/', dashboard, name='dashboard'),
    path('/listar_produtos', listar_produtos, name='listar_produtos'),
    path('/listar_marcas', listar_marcas, name="listar_marcas"),
    path('/criar_produto', criar_produto, name ="criar_produto"),
    path('/produto_editar/<int:id>/', produto_editar, name="produto_editar"),
    path('/produto_remover/<int:id>/', produto_remover, name="produto_remover"),
    path('/listar_marcas', listar_marcas, name='listar_marcas'),
    path('/criar_marca', criar_marca, name="criar_marca"),
    path('/marca_editar/<int:id>/', marca_editar, name="marca_editar"),
    path('/marca_remover/<int:id>/', marca_remover, name="marca_remover")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
