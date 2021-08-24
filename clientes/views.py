from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ClienteListView(ListView):
    model = Cliente
    context_object_name = 'lista_clientes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'active'
        return context


@method_decorator(login_required, name='dispatch')
class ClienteCreate(View):
    def get(self, request):
        form = ClienteForm()
        return render(request, 'clientes/cliente_form.html',
            {'form': form})

    def post(self, request):
        Cliente.objects.create(
            nome=request.POST['nome'], data_nasc=request.POST['data_nasc'],
            telefone=request.POST['telefone'], endereco=request.POST['endereco']
        )
        return redirect(reverse_lazy('cliente-list'))


@method_decorator(login_required, name='dispatch')
class ClienteUpdate(View):
    def get(self, request, pk):
        cliente = Cliente.objects.get(id=pk)
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/cliente_form.html', {'form': form})
    
    def post(self, request, pk):
        cliente = Cliente.objects.get(id=pk)
        cliente.nome = request.POST['nome']
        cliente.data_nasc = request.POST['data_nasc']
        cliente.telefone = request.POST['telefone']
        cliente.endereco = request.POST['endereco']
        cliente.save()
        return redirect(reverse_lazy('cliente-list'))


@method_decorator(login_required, name='dispatch')
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente-list')