from django import forms
from django.forms import fields, widgets
from .models import NotaServico


class NotaServicoForm(forms.ModelForm):
    data = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            format='%Y-%m-%d', attrs={'type': 'date'}),
    )
    class Meta:
        model = NotaServico
        fields = ['cliente', 'pagamento', 'servicos', 'data', 'valor', 'desconto']
