from django import forms
from .models import Compra, ItemCompra, ParcelaCompra
from datetime import date

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['num_compra', 'nfiscal', 'nparcelas', 'fornecedor']
        labels = {
            'nfiscal': 'Nota fiscal',
            'nparcelas': 'Parcelas',
        }


class ItemCompraForm(forms.ModelForm):
    class Meta:
        model = ItemCompra
        fields = ['produto', 'qtde']
        labels = {
            'qdte': 'Quantidade'
        }


class ParcelaCompraForm(forms.ModelForm):
    class Meta:
        model = ParcelaCompra
        fields = ['valor', 'datapagto', 'datavecto']
        labels = {
            'datapagto': 'Data de pagamento',
            'datavecto': 'Data de vencimento',
        }