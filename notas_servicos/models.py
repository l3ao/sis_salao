from django.db import models
from servicos.models import Servico
from clientes.models import Cliente


# Create your models here.
class NotaServico(models.Model):
    descricao = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ['-data', 'cliente__nome']


class ItemNotaServico(models.Model):
    notaservico = models.ForeignKey(NotaServico, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

