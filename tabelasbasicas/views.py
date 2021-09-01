from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Categoria, UnidMedida, TipoPagamento
# from .forms import ProdutoForm, CategoriaForm, UnidMedidaForm
# Create your views here.

@method_decorator(login_required, name='dispatch')
class CategoriaList(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'categoria/categoria_list.html'


@method_decorator(login_required, name='dispatch')
class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['sigla', 'descricao']
    success_url = reverse_lazy('categoria-list')
    template_name = 'categoria/categoria_form.html'


@method_decorator(login_required, name='dispatch')
class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['sigla', 'descricao']
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria-list')


@method_decorator(login_required, name='dispatch')
class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria-list')
    template_name = 'categoria/categoria_confirm_delete.html'


@method_decorator(login_required, name='dispatch')
class UnidMedidaList(ListView):
    model = UnidMedida
    context_object_name = 'unidmedidas'
    template_name = 'unidmedida/unidmedida_list.html'


@method_decorator(login_required, name='dispatch')
class UnidMedidaCreate(CreateView):
    model = UnidMedida
    fields = ['sigla', 'descricao']
    success_url = reverse_lazy('unidmedida-list')
    template_name = 'unidmedida/unidmedida_form.html'


@method_decorator(login_required, name='dispatch')
class UnidMedidaUpdate(UpdateView):
    model = UnidMedida
    fields = ['sigla', 'descricao']
    success_url = reverse_lazy('unidmedida-list')
    template_name = 'unidmedida/unidmedida_form.html'


@method_decorator(login_required, name='dispatch')
class UnidMedidaDelete(DeleteView):
    model = UnidMedida
    success_url = reverse_lazy('unidmedida-list')
    template_name = 'unidmedida/unidmedida_confirm_delete.html'


@method_decorator(login_required, name='dispatch')
class TipoPagamentoList(ListView):
    model = TipoPagamento
    template_name = 'tipopagamento/tipopagamento_list.html'


@method_decorator(login_required, name='dispatch')
class TipoPagamentoCreate(CreateView):
    model = TipoPagamento
    fields = ['sigla', 'descricao']
    success_url = reverse_lazy('tipopagamento-list')
    template_name = 'tipopagamento/tipopagamento_form.html'


@method_decorator(login_required, name='dispatch')
class TipoPagamentoUpdate(UpdateView):
    model = TipoPagamento
    fields = ['sigla', 'descricao']
    success_url = reverse_lazy('tipopacategoriagamento-list')
    template_name = 'tipopagamento/tipopagamento_form.html'


@method_decorator(login_required, name='dispatch')
class TipoPagamentoDelete(DeleteView):
    model = TipoPagamento
    success_url = reverse_lazy('tipopagamento-list')
    template_name = 'tipopagamento/tipopagamento_confirm_delete.html'
