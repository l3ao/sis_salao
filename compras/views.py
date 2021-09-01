from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from compras import models
from .forms import CompraForm, ItemCompraForm, ParcelaCompraForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class CompraList(generic.ListView):
    paginate_by = 10
    model = models.Compra
    context_object_name = 'compras'
    ordering = '-num_compra'


@method_decorator(login_required, name='dispatch')
class CompraCreate(generic.View):
    def get(self, request):
        form = CompraForm()
        return render(request, 'compras/compra_form.html', {'form': form})

    def post(self, request):
        data = {}
        if request.POST['compra_id']:
            compra = models.Compra.objects.get(id=request.POST['compra_id'])
            compra.nfiscal = request.POST['nfiscal']
            compra.nparcelas = request.POST['nparcelas']
            compra.fornecedor_id = request.POST['fornecedor']
            compra.save()
        else:
            num_compra = str(models.Compra.objects.count() + 1).zfill(5)
            compra = models.Compra.objects.create(
                num_compra=num_compra,
                nfiscal=request.POST['nfiscal'],
                nparcelas=request.POST['nparcelas'],
                fornecedor_id=request.POST['fornecedor']
            )

        form = CompraForm(instance=compra)
        form_item = ItemCompraForm()
        data['compra'] = compra
        data['itens'] = compra.itemcompra_set.all()
        data['form'] = form
        data['form_item'] = form_item
        return render(request, 'compras/compra_form.html', data)


@method_decorator(login_required, name='dispatch')
class CompraUpdate(generic.View):
    def get(self, request, compra):
        data = {}
        compra = models.Compra.objects.get(id=compra)
        form = CompraForm(instance=compra)
        form_item = ItemCompraForm()
        data['compra'] = compra
        data['itens'] = compra.itemcompra_set.all()
        data['form'] = form
        data['form_item'] = form_item
        return render(request, 'compras/compra_form.html', data)

    def post(self, request, compra):
        pass


@method_decorator(login_required, name='dispatch')
class CompraDelete(generic.View):
    def get(self, request, compra):
        compra = models.Compra.objects.get(id=compra)
        return render(request, 'compras/compra_confirm_delete.html', {'compra': compra})

    def post(self, request, compra):
        compra = models.Compra.objects.get(id=compra)
        compra.delete()
        return redirect('compra-list')


@method_decorator(login_required, name='dispatch')
class ItemCompraCreate(generic.View):
    def get(self, request):
        pass

    def post(self, request, compra):
        data = {}

        item = models.ItemCompra.objects.filter(
            compra_id=compra, produto_id=request.POST['produto']
        )

        if item:
            data['mensagem'] = 'Produto já cadastrado'
            item = item[0]
        else:
            produto = models.Produto.objects.get(id=request.POST['produto'])
            item = models.ItemCompra.objects.create(
                qtde=request.POST['qtde'], valor=produto.valorpago,
                compra_id=compra, produto_id=request.POST['produto']
            )
        data['compra'] = item.compra
        data['itens'] = item.compra.itemcompra_set.all()
        data['form'] = CompraForm(instance=item.compra)
        data['form_item'] = ItemCompraForm()
        return render(request, 'compras/compra_form.html', data)


@method_decorator(login_required, name='dispatch')
class ItemCompraUpdate(generic.View):
    def get(self, request, itemcompra):
        item = models.ItemCompra.objects.get(id=itemcompra)
        form = ItemCompraForm(instance=item)
        return render(request, 'compras/itemcompra_form.html', {'form': form, 'item': item})

    def post(self, request, itemcompra):
        item = models.ItemCompra.objects.get(id=itemcompra)
        produto = models.Produto.objects.get(id=request.POST['produto'])
        item.qtde = request.POST['qtde']
        item.valor = produto.valorpago
        item.produto_id = request.POST['produto']
        item.save()
        return redirect('compra-update', item.compra.id)


@method_decorator(login_required, name='dispatch')
class ItemCompraDelete(generic.View):
    def get(self, request, itemcompra):
        item = models.ItemCompra.objects.get(id=itemcompra)
        return render(request, 'compras/itemcompra_confirm_delete.html', {'item': item})

    def post(self, request, itemcompra):
        item = models.ItemCompra.objects.get(id=itemcompra)
        compra_id = item.compra_id
        item.delete()
        return redirect('compra-update', compra_id)


@method_decorator(login_required, name='dispatch')
class FinalizarCompraView(generic.View):
    def get(self, request, compra):
        compra = models.Compra.objects.get(id=compra)
        compra.gerarestoque()
        compra.gerar_pagamento()
        return redirect('compra-list')


@method_decorator(login_required, name='dispatch')
class PagamentoList(generic.View):
    def get(self, request):
        compras = models.Compra.objects.all()
        return render(request, 'compras/pagamento_list.html', {'compras': compras})


@method_decorator(login_required, name='dispatch')
class PagamentoDetail(generic.View):
    def get(self, request, compra):
        data = {}
        compra = models.Compra.objects.get(id=compra)
        parcelas_compra = models.ParcelaCompra.objects.filter(compra=compra)
        data['compra'] = compra
        data['parc_compra'] = parcelas_compra
        return render(request, 'compras/pagamento_form.html', data)


@method_decorator(login_required, name='dispatch')
class PagarParcCompra(generic.View):
    def get(self, request, parccompra):
        parcelacompra = models.ParcelaCompra.objects.get(id=parccompra)
        form = ParcelaCompraForm(instance=parcelacompra)
        return render(request, 'compras/parcela_compra_form.html', {'form': form})

    def post(self, request, parccompra):
        parcelacompra = models.ParcelaCompra.objects.get(id=parccompra)
        parcelacompra.datapagto = request.POST['datapagto']
        parcelacompra.save()
        return redirect('pagamento-detail', parcelacompra.compra_id)
