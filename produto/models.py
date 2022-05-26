from math import prod
from django.db import models

class Cores(models.Model):
    cor = models.CharField('Cor', max_length=200)

    def __str__(self):
        return self.cor


class Produtos(models.Model):
    produto = models.CharField('Produto', max_length=200)
    cor = models.ForeignKey(Cores, on_delete=models.PROTECT, verbose_name='Cor')
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=12, default=0)
    quantidade = models.IntegerField('Quantidade', default=0)


    criado = models.DateTimeField('Criado', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now_add=True)

    def __str__(self):
        return self.produto
