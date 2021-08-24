from django import forms
from django.db.models import fields
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'rsocial', 'ie', 'cnpj', 'cep', 'endereco',
                  'bairro', 'fone', 'cel', 'email', 'endnumero', 'cidade', 'estado']
        labels = {
            'rsocial': 'Razão social',
            'ie': 'Insc. Estadual',
            'cnpj': 'CNPJ',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'fone': 'Telefone',
            'cel': 'Celular',
            'email': 'E-mail',
            'endnumero': 'Número',
        }