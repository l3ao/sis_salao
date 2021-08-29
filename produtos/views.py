from django.core import paginator
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView
from django.core.paginator import Paginator
from .models import Produto, Categoria, UnidMedida
from .forms import ProdutoForm, CategoriaForm, UnidMedidaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProdutoList(ListView):
    model = Produto
    context_object_name = 'produtos'

    def get(self, request, *args, **kwargs):
        # super().get(request, *args, **kwargs)
        termo_busca = request.GET.get('pesquisa', None)
        if termo_busca:
            produtos = Produto.objects.filter(descricao__icontains=termo_busca)
        else:
            produtos_list = Produto.objects.all()
            paginator = Paginator(produtos_list, 15)
            page = request.GET.get('page')
            produtos = paginator.get_page(page)
        return render(request, 'produtos/produto_list.html', {'produtos': produtos})


@method_decorator(login_required, name='dispatch')
class ProdutoCreate(View):
    def get(self, request):
        form = ProdutoForm()
        return render(request, 'produtos/produto_form.html', {'form': form})

    def post(self, request):
        Produto.objects.create(
                descricao=request.POST['descricao'], valorpago=request.POST['valorpago'],
                valorvenda=request.POST['valorvenda'], categoria_id=request.POST['categoria'],
                und_medida_id=request.POST['und_medida']
            )
        return redirect(reverse_lazy('produto-list'))


@method_decorator(login_required, name='dispatch')
class ProdutoUpdate(View):
    def get(self, request, pk):
        produto = Produto.objects.get(id=pk)
        form = ProdutoForm(instance=produto)
        return render(request, 'produtos/produto_form.html', {'form': form})

    def post(self, request, pk):
        produto = Produto.objects.get(id=pk)
        produto.descricao = request.POST['descricao']
        produto.valorpago = request.POST['valorpago']
        produto.valorvenda = request.POST['valorvenda']
        produto.categoria_id = request.POST['categoria']
        produto.und_medida_id = request.POST['und_medida']
        produto.save()
        return redirect(reverse_lazy('produto-list'))


@method_decorator(login_required, name='dispatch')
class ProdutoDelete(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto-list')


@method_decorator(login_required, name='dispatch')
class CategoriaList(ListView):
    model = Categoria
    context_object_name = 'categorias'


@method_decorator(login_required, name='dispatch')
class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produtos/categoria_form.html'
    success_url = reverse_lazy('categoria-list')


@method_decorator(login_required, name='dispatch')
class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produtos/categoria_form.html'
    success_url = reverse_lazy('categoria-list')


@method_decorator(login_required, name='dispatch')
class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria-list')


@method_decorator(login_required, name='dispatch')
class UnidMedidaList(ListView):
    model = UnidMedida
    context_object_name = 'unidmedidas'


@method_decorator(login_required, name='dispatch')
class UnidMedidaCreate(CreateView):
    model = UnidMedida
    fields = ['sigla', 'nome']
    success_url = reverse_lazy('unidmedida-list')


@method_decorator(login_required, name='dispatch')
class UnidMedidaUpdate(UpdateView):
    model = UnidMedida
    fields = ['sigla', 'nome']
    success_url = reverse_lazy('unidmedida-list')


@method_decorator(login_required, name='dispatch')
class UnidMedidaDelete(DeleteView):
    model = UnidMedida
    success_url = reverse_lazy('unidmedida-list')
