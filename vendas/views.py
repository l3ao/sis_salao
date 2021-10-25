from compras.models import TipoPagamento
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from .models import NegociacaoParcela, Venda, ItemDaVenda, Produto, ParcelaVenda
from .forms import VendaForm, ItemDaVendaForm, ParcelaForm, RealizarPagamentoForm
from django.db.models import Count, Sum
from clientes.models import Cliente
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class VendaView(ListView):
    paginate_by = 10
    model = Venda
    context_object_name = 'vendas'
    ordering = '-num_venda'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=2)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendas_abertas = Venda.objects.filter(status=1)
        context['vendas_abertas'] = vendas_abertas
        return context


@method_decorator(login_required, name='dispatch')
class VendaCreate(View):
    def get(self, request):
        form = VendaForm()
        return render(request, 'vendas/venda_form.html', {'form_venda': form})

    def post(self, request):
        data = {}
        venda_id = request.POST.get('venda_id', None)

        if venda_id:
            venda = Venda.objects.get(id=venda_id)
            venda.nparcelas = request.POST['nparcelas']
            venda.cliente_id = request.POST['cliente']
            venda.save()
        else:
            vendas = Venda.objects.order_by('id').last()
            num_venda = vendas.id + 1 if vendas else 1
            venda = Venda.objects.create(
                num_venda=str(num_venda).zfill(5),
                nparcelas=request.POST['nparcelas'],
                cliente_id=request.POST['cliente'],
            )

        form_venda = VendaForm(instance=venda)
        form_item = ItemDaVendaForm()
        data['venda'] = venda
        data['itens'] = venda.itemdavenda_set.all()
        data['form_venda'] = form_venda
        data['form_item'] = form_item

        return render(request, 'vendas/venda_form.html', data)


@method_decorator(login_required, name='dispatch')
class VendaUpdate(View):
    def get(self, request, venda):
        data = {}

        venda = Venda.objects.get(id=venda)
        itens = venda.itemdavenda_set.all()
        form_venda = VendaForm(instance=venda)
        form_item = ItemDaVendaForm()

        data['venda'] = venda
        data['itens'] = venda.itemdavenda_set.all()
        data['form_venda'] = form_venda
        data['form_item'] = form_item

        return render(request, 'vendas/venda_form.html', data)

    def post(self, request, venda):
        pass

# retirar venda delete
# adicionar detail(visualizacao da venda)
@method_decorator(login_required, name='dispatch')
class VendaDelete(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(request, 'vendas/venda_confirm_delete.html', {'venda': venda})

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)
        venda.delete()
        return redirect('venda-list')


@method_decorator(login_required, name='dispatch')
class ItemVendaCreate(View):
    def post(self, request, venda):
        data = {}
        produto = Produto.objects.get(id=request.POST['produto'])
        estoque = produto.estoque - int(request.POST['qtde'])
        item = ItemDaVenda.objects.filter(
            venda_id=venda, produto_id=request.POST['produto'])

        mensagem = ''
        if item.exists(): # existencia
            mensagem = 'Item já cadastrado.'
        elif estoque < 0: # verificar estoque
            mensagem = 'Produto tem estoque atual de: 0{}'.format(produto.estoque)
        
        if mensagem:
            venda = item[0].venda if item.exists() else Venda.objects.get(id=venda)
            data['mensagem'] = mensagem
            data['venda'] = venda
            data['itens'] = venda.itemdavenda_set.all()
            data['form_venda'] = VendaForm(instance=venda)
            data['form_item'] = ItemDaVendaForm()
        
        if not item.exists() and estoque >= 0:
            item = ItemDaVenda.objects.create(
                qtde=request.POST['qtde'], valor=produto.valorvenda,
                venda_id=venda, produto_id=request.POST['produto'],)

            data['venda'] = item.venda
            data['itens'] = item.venda.itemdavenda_set.all()
            data['form_venda'] = VendaForm(instance=item.venda)
            data['form_item'] = ItemDaVendaForm()

        return render(request, 'vendas/venda_form.html', data)


@method_decorator(login_required, name='dispatch')
class ItemVendaUpdate(View):
    def get(self, request, itemvenda):
        data = {}
        item = ItemDaVenda.objects.get(id=itemvenda)
        form = ItemDaVendaForm(instance=item)
        data['item'] = item
        data['form'] = form

        return render(request, 'vendas/itemvenda_form.html', data)


    def post(self, request, itemvenda):
        item = ItemDaVenda.objects.get(id=itemvenda)
        produto = Produto.objects.get(id=request.POST['produto'])
        data = {}
        mensagem = ''
        # verifica produto
        if item.produto.id != produto.id:
            if ItemDaVenda.objects.filter(venda=item.venda, produto=produto).exists():
                mensagem = 'Produto já está cadastrado'
        # verifica estoque
        if not mensagem:
            estoque = produto.estoque - int(request.POST['qtde'])
            if estoque < 0:
                mensagem = f'Produto tem estoque atual de: 0{str(produto.estoque)}'
        
        if mensagem:
            form = ItemDaVendaForm(instance=item)
            data['item'] = item
            data['form'] = form
            data['mensagem'] = mensagem
            return render(request, 'vendas/itemvenda_form.html', data)

        item.qtde = request.POST['qtde']
        item.valor = produto.valorvenda
        item.produto_id = request.POST['produto']
        item.save()
        return redirect('venda-update', venda=item.venda_id)


@method_decorator(login_required, name='dispatch')
class ItemVendaDelete(View):
    def get(self, request, itemvenda):
        item = ItemDaVenda.objects.get(id=itemvenda)
        return render(request, 'vendas/itemvenda_confirm_delete.html', {'item': item})

    def post(self, request, itemvenda):
        item = ItemDaVenda.objects.get(id=itemvenda)
        venda_id = item.venda_id
        item.delete()
        return redirect('venda-update', venda=venda_id)


@method_decorator(login_required, name='dispatch')
class FinalizarVendaView(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        # verificar estoque
        mensagem = ''
        itens = venda.itemdavenda_set.all()
        for item in itens:
            produto = Produto.objects.get(id=item.produto.id)
            estoque = produto.estoque - item.qtde
            if estoque < 0:
                mensagem = f'{produto.descricao} tem estoque atual de: 0{str(produto.estoque)}'
                break

        if mensagem:
            data = {}
            itens = venda.itemdavenda_set.all()
            form_venda = VendaForm(instance=venda)
            form_item = ItemDaVendaForm()

            data['venda'] = venda
            data['itens'] = venda.itemdavenda_set.all()
            data['form_venda'] = form_venda
            data['form_item'] = form_item
            data['mensagem'] = mensagem
            return render(request, 'vendas/venda_form.html', data)
        else:
            venda.finalizar()
            return redirect('venda-list')


@method_decorator(login_required, name='dispatch')
class RecebimentoList(View):
    def get(self, request):
        vendas = Venda.objects.values('cliente__nome', 'cliente_id').annotate(qt_vendas=Count('cliente'), total=Sum('total')).order_by()
        return render(request, 'vendas/recebimento_list.html', {'vendas': vendas})


@method_decorator(login_required, name='dispatch')
class RecebimentoDetail(View):
    def get(self, request, cliente):
        data = {}
        data['cliente'] = Cliente.objects.get(id=cliente)
        data['parcelas'] = ParcelaVenda.objects \
            .filter(venda__cliente_id=cliente) \
            .order_by('-datapagto', 'datavecto')
        recebimento = ParcelaVenda.objects.values('venda__cliente__nome', 'venda__cliente_id') \
            .annotate(qt_parcelas=Count('id'), total=Sum('valor')) \
            .filter(venda__cliente_id=cliente, status__in=['AV', 'VD'])
        if recebimento.exists():
            data['recebimento'] = recebimento[0]
        return render(request, 'vendas/recebimento_detail.html', data)


@method_decorator(login_required, name='dispatch')
class RecebimentoParcela(View):
    def get(self, request, parcela):
        data = {}
        parcela = ParcelaVenda.objects.get(id=parcela)
        form = ParcelaForm(instance=parcela)
        data['venda_id'] = parcela.venda.id
        data['parcela_id'] = parcela.id
        data['form'] = form
        return render(request, 'vendas/parcela_form.html', data)

    def post(self, request, parcela):
        parcela = ParcelaVenda.objects.get(id=parcela)
        parcela.datapagto = request.POST['datapagto']
        parcela.status = 'PG'
        parcela.pagamento_id = request.POST['pagamento']
        parcela.save()
        return redirect('recebimento-detail', parcela.venda.id)


@method_decorator(login_required, name='dispatch')
class NegociacaoParcelaView(View):
    def get(self, request, parcela):
        data = {}
        parcelavenda = ParcelaVenda.objects.get(id=parcela)
        data['parcela'] = parcela
        data['venda_id'] = parcelavenda.venda.id
        # data['form'] = NegociacaoForm()
        return render(request, 'vendas/negociar_parcela_form.html', data)
    
    def post(self, request, parcela):
        parcela = ParcelaVenda.objects.get(id=parcela)
        negociacao = NegociacaoParcela.objects.create(
            parcela=parcela, pagamento_id=request.POST['pagamento'],
            valor_negoc=request.POST['valor_negoc'], qtde_parcelas=request.POST['qtde_parcelas'],
            datavecimento=request.POST['datavencimento']
        )
        negociacao.negociar()
        parcela.datapagto = datetime.now()
        parcela.status = 'PG'
        parcela.pagamento_id = request.POST['pagamento']
        parcela.save()
        return redirect('recebimento-detail', parcela.venda.id)


@method_decorator(login_required, name='dispatch')
class RealizarPagamentoView(View):
    def get(self, request, cliente):
        data = {}
        form = RealizarPagamentoForm()
        data['form'] = form
        data['cliente_id'] = cliente
        return render(request, 'vendas/realizar_pagamento_form.html', data)

    def post(self, request, cliente):
        valorpago = float(request.POST['valor'])
        datapagto = datetime.strptime(request.POST['data'], '%Y-%m-%d')
        tipopagamento = request.POST['tipopagamento']
        parcelas = ParcelaVenda.objects.filter(venda__cliente_id=cliente, status__in=['AV', 'VD']).order_by('datavecto')
        # nao está fucionando data de vencimento
        for parcela in parcelas:
            parcela.datapagto = datapagto
            parcela.valorpago = parcela.valor if valorpago >= parcela.valor else valorpago
            parcela.status = 'PG'
            parcela.pagamento_id = tipopagamento
            parcela.save()

            if parcela.valor > valorpago:
                negociacao = NegociacaoParcela.objects.create(
                    parcela=parcela, valor_negoc=valorpago,
                )
                datavenc = datapagto+timedelta(30)
                negociacao.negociar(datavenc=datavenc)
            
            valorpago = valorpago - float(parcela.valor)

            if valorpago <= 0:
                break
        
        return redirect('recebimento-detail', cliente)
