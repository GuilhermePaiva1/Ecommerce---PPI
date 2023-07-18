from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    informacoes = models.TextField(max_length=500)
    preco = models.FloatField()
    img = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.nome