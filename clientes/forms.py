from django import forms
from django.forms import fields
from .models import Cliente

class ClienteForm(forms.ModelForm):
    data_nasc = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date'}),
    )
    class Meta:
        model = Cliente
        fields = ['nome', 'data_nasc', 'telefone', 'endereco']
        labels = {
            'endereco': 'Endereço',
        }
