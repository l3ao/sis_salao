from django.db import models
from django.db.models import F, FloatField, Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from fornecedores.models import Fornecedor
from produtos.models import Produto
import datetime


# Create your models here.
class TipoPagamento(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=3, blank=True, null=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Compra(models.Model):
    num_compra = models.CharField(verbose_name='Número', blank=True, null=True, max_length=10)
    nfiscal = models.IntegerField(verbose_name='Número NF-e')
    data = models.DateField(verbose_name='Data de criação', auto_now=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    nparcelas = models.IntegerField(verbose_name='Parcelas', default=1)
    fornecedor = models.ForeignKey(Fornecedor, verbose_name='Fornecedor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data', 'fornecedor__nome']

    def calcular_total(self):
        tot = self.itemcompra_set.all().aggregate(
            tot_ped=Sum(F('qtde') * F('valor'),
                        output_field=FloatField())
        )['tot_ped'] or 0

        self.total = tot
        Compra.objects.filter(id=self.id).update(total=tot)

    def gerarestoque(self):
        itens = self.itemcompra_set.all()
        for item in itens:
            produto = Produto.objects.get(id=item.produto_id)
            est_inicial = produto.estoque
            produto.estoque = est_inicial + item.qtde
            produto.save()

    def gerar_pagamento(self):
        nparcelas = int(self.nparcelas)
        if nparcelas >= 1:
            valorparc = self.total / nparcelas
            dataparc = datetime.date(year=self.data.year, month=self.data.month, day=self.data.day)
            dias = datetime.timedelta(days=30)
            for i in range(nparcelas):
                dataparc += dias
                ParcelaCompra.objects.create(
                    valor=valorparc, datavecto=dataparc, compra_id=self.id
                )


class ItemCompra(models.Model):
    qtde = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.descricao


class ParcelaCompra(models.Model):
    PAGO = 'PG'
    VENCIDO = 'VD'
    AVENCER = 'AV'

    STATUS_CHOICES = [
        (PAGO, 'Pago'),
        (VENCIDO, 'Vencido'),
        (AVENCER, 'A vencer'),
    ]

    valor = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    datapagto = models.DateField(null=True)
    datavecto = models.DateField()
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=AVENCER,
        blank=True, null=True
    )
    pagamento = models.ForeignKey(TipoPagamento, on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=Compra)
def update_compra_total(sender, instance, **kwargs):
    instance.calcular_total()


@receiver(post_delete, sender=ItemCompra)
def update_compra_total(sender, instance, **kwargs):
    instance.compra.calcular_total()


@receiver(post_save, sender=ItemCompra)
def update_itemcompra_total(sender, instance, **kwargs):
    instance.compra.calcular_total()
