from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .models import Fornecedor
from .forms import FornecedorForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class FornecedorList(generic.ListView):
    model = Fornecedor


@method_decorator(login_required, name='dispatch')
class FornecedorCreate(generic.View):
    # model = Fornecedor
    # fields = ['nome', 'rsocial', 'ie', 'cnpj', 'cep', 'endereco', 'endnumero',
    #           'bairro', 'cidade', 'estado', 'fone', 'cel', 'email']
    # success_url = reverse_lazy('fornecedor-list')
    def get(self, request):
        form = FornecedorForm()
        return render(request, 'fornecedores/fornecedor_form.html', {'form': form})
    
    def post(self, request):
        Fornecedor.objects.create(
            nome=request.POST['nome'], rsocial=request.POST['rsocial'], ie=request.POST['ie'],
            cnpj=request.POST['cnpj'],cep=request.POST['cep'],endereco=request.POST['endereco'],
            endnumero=request.POST['endnumero'],bairro=request.POST['bairro'],estado=request.POST['estado'],
            fone=request.POST['fone'],cel=request.POST['cel'],email=request.POST['email'],
        )
        return redirect(reverse_lazy('fornecedor-list'))


@method_decorator(login_required, name='dispatch')
class FornecedorUpdate(generic.UpdateView):
    def get(self, request, pk):
        fornecedor = Fornecedor.objects.get(id=pk)
        form = FornecedorForm(instance=fornecedor)
        return render(request, 'fornecedores/fornecedor_form.html', {'form': form})
    
    def post(self, request, pk):
        fornecedor = Fornecedor.objects.get(id=pk)
        fornecedor.nome=request.POST['nome']
        fornecedor.rsocial=request.POST['rsocial']
        fornecedor.ie=request.POST['ie']
        fornecedor.cnpj=request.POST['cnpj']
        fornecedor.cep=request.POST['cep']
        fornecedor.endereco=request.POST['endereco']
        fornecedor.endnumero=request.POST['endnumero']
        fornecedor.bairro=request.POST['bairro']
        fornecedor.estado=request.POST['estado']
        fornecedor.fone=request.POST['fone']
        fornecedor.cel=request.POST['cel']
        fornecedor.email=request.POST['email']
        fornecedor.save()
        return redirect(reverse_lazy('fornecedor-list'))


@method_decorator(login_required, name='dispatch')
class FornecedorDelete(generic.DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedor-list')