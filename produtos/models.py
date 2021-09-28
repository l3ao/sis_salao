from django.db import models
from tabelasbasicas.models import Categoria, UnidMedida

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    desc_nf = models.CharField(max_length=100, null=True, blank=True)
    valorpago = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    valorvenda = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    und_medida = models.ForeignKey(UnidMedida, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.desc_nf + ' - Estoque: ' + str(self.estoque)

    class Meta:
        ordering = ['descricao']
