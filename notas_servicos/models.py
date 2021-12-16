from django.db import models
from servicos.models import Servico
from clientes.models import Cliente
from tabelasbasicas.models import TipoPagamento

# Create your models here.
class NotaServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(TipoPagamento,
        on_delete=models.CASCADE, blank=True, null=True)
    servicos = models.ManyToManyField(Servico,
        blank=True, null=True)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)    

    class Meta:
        ordering = ['-data', 'cliente__nome']

