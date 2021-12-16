from produtos.models import Produto
from django import forms
from django.forms import ModelForm, Form
from .models import NegociacaoParcela, ParcelaVenda, Venda, ItemDaVenda
from compras.models import TipoPagamento
from datetime import date

class VendaForm(ModelForm):

    class Meta:
        model = Venda
        fields = ['num_venda', 'total', 'nparcelas', 'cliente']
        labels = {
            'nparcelas': 'Nº de parcelas',
            'num_venda': 'Número da venda'
        }


class ItemDaVendaForm(ModelForm):
    produto = forms.ModelChoiceField(Produto.objects.filter(estoque__gte=1), required=True)
    qtde = forms.IntegerField(label='Quantidade', required=True, min_value=0)
    class Meta:
        model = ItemDaVenda
        fields = ['produto', 'qtde']


class ParcelaForm(ModelForm):
    datapagto = forms.DateField(
        required=True,
        label='Data de pagamento',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'value': date.today()}),
    )
    datavecto = forms.DateField(
        label='Data de vencimento',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date',}),
    )
    pagamento = forms.ModelChoiceField(TipoPagamento.objects.all(), required=True)
    class Meta:
        model = ParcelaVenda
        fields = ['valor', 'datapagto', 'datavecto', 'pagamento', 'status']


class RealizarPagamentoForm(Form):
    valor = forms.DecimalField(label='Valor',
        max_digits=5, decimal_places=2, initial=0, min_value=1)
    data = forms.DateField(
        required=True,
        label='Data de pagamento',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date', 'value': date.today()}),
    )
    tipopagamento = forms.ModelChoiceField(TipoPagamento.objects.all(),
        label='Forma de pagamento')