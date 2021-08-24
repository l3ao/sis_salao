from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Servico
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ServicoList(ListView):
    model = Servico
    context_object_name = 'servicos'


@method_decorator(login_required, name='dispatch')
class ServicoCreate(CreateView):
    model = Servico
    fields = ['descricao', 'preco']
    success_url = reverse_lazy('servico-list')


@method_decorator(login_required, name='dispatch')
class ServicoUpdate(UpdateView):
    model = Servico
    fields = ['descricao', 'preco']
    success_url = reverse_lazy('servico-list')


@method_decorator(login_required, name='dispatch')
class ServicoDelete(DeleteView):
    model = Servico
    success_url = reverse_lazy('servico-list')
