from django.db import models


# Create your models here.
class Categoria(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=2)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class UnidMedida(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=2)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class TipoPagamento(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=3)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
