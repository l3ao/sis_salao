from django.db import models


# Create your models here.
class Categoria(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=2, blank=True, null=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class UnidMedida(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=2, blank=True, null=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    valorpago = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valorvenda = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    und_medida = models.ForeignKey(UnidMedida, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descricao + ' - Estoque: ' + str(self.estoque)

    class Meta:
        ordering = ['descricao']
