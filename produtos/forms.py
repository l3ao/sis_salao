
from django import forms
from django.forms import ModelForm, DecimalField
from django.forms.fields import CharField
from .models import Produto, Categoria, UnidMedida


class CategoriaForm(ModelForm):
    sigla = CharField(label='Sigla', required=True, max_length=2)
    descricao = CharField(label='Descrição', required=True)

    class Meta:
        model = Categoria
        fields = ['sigla', 'descricao']


class UnidMedidaForm(ModelForm):
    sigla = CharField(label='Sigla', required=True, max_length=2)
    descricao = CharField(label='Descrição', required=True)

    class Meta:
        model = UnidMedida
        fields = ['sigla', 'descricao']


class ProdutoForm(ModelForm):
    valorpago = DecimalField(label='Valor de compra', required=True,
                            max_digits=10, decimal_places=2, min_value=0)
    valorvenda = DecimalField(label='Valor de venda', required=True,
                            max_digits=10, decimal_places=2, min_value=0)
    descricao = CharField(label='Descrição do produto', required=True)
    class Meta:
        model = Produto
        fields = ['valorpago', 'valorvenda',
                  'estoque', 'categoria', 'und_medida', 'descricao']
        labels = {
            'und_medida': 'Unidade de medida',
        }
