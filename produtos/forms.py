
from django import forms
from django.forms import ModelForm, DecimalField
from .models import Produto


class ProdutoForm(ModelForm):
    valorpago = DecimalField(label='Valor de compra', required=True,
                            max_digits=10, decimal_places=2, min_value=0)
    valorvenda = DecimalField(label='Valor de venda', required=True,
                            max_digits=10, decimal_places=2, min_value=0)
    class Meta:
        model = Produto
        fields = ['descricao', 'valorpago', 'valorvenda',
                  'estoque', 'categoria', 'und_medida']
        labels = {
            'und_medida': 'Unidade de medida',
        }
