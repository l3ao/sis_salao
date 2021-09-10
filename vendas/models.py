import datetime
from django.db import models
from django.db.models import Sum, F, FloatField
from django.db.models.signals import post_save
from django.dispatch import receiver
from clientes.models import Cliente
from produtos.models import Produto
from compras.models import TipoPagamento


# Create your models here.
class Venda(models.Model):
    ABERTA = 1
    FINALIZADA = 2

    STATUS_VENDA = [
        (ABERTA, 'Aberta'),
        (FINALIZADA, 'Finalizada'),
    ]

    num_venda = models.CharField(verbose_name='Número da venda',
        unique=True, max_length=10, blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True, blank=True, null=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    nparcelas = models.IntegerField(default=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=STATUS_VENDA,
        default=ABERTA,
    )

    class Meta:
        ordering = ['-data_criacao', 'cliente__nome']

    def calcular_total(self):
        tot = self.itemdavenda_set.all().aggregate(
            tot_ped=Sum(F('qtde') * F('produto__valorvenda'),
                        output_field=FloatField())
        )['tot_ped'] or 0
        self.total = tot
        Venda.objects.filter(id=self.id).update(total=tot)

    def finalizar(self):
        self.status = 2
        self.save()
        self.mov_estoque()
        self.gerar_recebimento()

    def mov_estoque(self):
        itens = self.itemdavenda_set.all()
        for item in itens:
            produto = Produto.objects.get(id=item.produto_id)
            est_inicial = produto.estoque
            produto.estoque = est_inicial - item.qtde
            produto.save()

    def gerar_recebimento(self):
        nparcelas = int(self.nparcelas)
        if nparcelas >= 1:
            valorparc = self.total / nparcelas
            dataparc = datetime.date(year=self.data_criacao.year, month=self.data_criacao.month, day=self.data_criacao.day)
            dias = datetime.timedelta(days=30)
            for i in range(nparcelas):
                dataparc += dias
                ParcelaVenda.objects.create(
                    valor=valorparc, datavecto=dataparc, venda_id=self.id
                )


class ItemDaVenda(models.Model):
    qtde = models.IntegerField(default=1)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.descricao

    class Meta:
        unique_together = [['venda', 'produto']]


class ParcelaVenda(models.Model):
    PAGA = 'PG'
    VENCIDA = 'VD'
    AVENCER = 'AV'

    STATUS_CHOICES = [
        (PAGA, 'Paga'),
        (VENCIDA, 'Vencida'),
        (AVENCER, 'A vencer'),
    ]

    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=AVENCER,
    )
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    valorpago = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    pagamento = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE, null=True)
    datapagto = models.DateField(null=True, blank=True)
    datavecto = models.DateField(null=True, blank=True)
    negociada = models.BooleanField(verbose_name='Parcela negociada', default=False,
        blank=True, null=True)


class NegociacaoParcela(models.Model):
    parcela = models.ForeignKey(ParcelaVenda, on_delete=models.CASCADE)
    valor_negoc = models.DecimalField(verbose_name='Valor da negocioção',
        max_digits=5, decimal_places=2, default=0)

    def negociar(self, datavenc):
        valor_parc = float(self.parcela.valor) - float(self.valor_negoc)
        ParcelaVenda.objects.create(
            venda_id=self.parcela.venda.id, status='AV', valor=valor_parc,
            datavecto=datavenc, negociada=True
        )


@receiver(post_save, sender=ItemDaVenda)
def update_itempedido_total(sender, instance, **kwargs):
    instance.venda.calcular_total()


@receiver(post_save, sender=Venda)
def update_venda_total(sender, instance, **kwargs):
    instance.calcular_total()
