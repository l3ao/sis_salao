from django.urls import path
from .views import (
    VendaView, VendaCreate, VendaUpdate, VendaDelete,
    ItemVendaCreate, ItemVendaUpdate, ItemVendaDelete, FinalizarVendaView,
    RecebimentoList, RecebimentoDetail, RecebimentoParcela, NegociacaoParcelaView, RealizarPagamentoView
)

urlpatterns = [
    path('', VendaView.as_view(), name='venda-list'),
    path('add/', VendaCreate.as_view(), name='venda-add'),
    path('venda/<int:venda>', VendaUpdate.as_view(), name='venda-update'),
    path('venda/<int:venda>/delete', VendaDelete.as_view(), name='venda-delete'),
    path('add-item/<int:venda>', ItemVendaCreate.as_view(), name='itemvenda-add'),
    path('item/<int:itemvenda>', ItemVendaUpdate.as_view(), name='itemvenda-update'),
    path('item/<int:itemvenda>/delete', ItemVendaDelete.as_view(), name='itemvenda-delete'),
    path('venda/finalizarvenda/<int:venda>/', FinalizarVendaView.as_view(), name='finalizar_venda'),
    path('recebimentos/', RecebimentoList.as_view(), name='recebimento-list'),
    path('recebimento/<int:cliente>', RecebimentoDetail.as_view(), name='recebimento-detail'),
    path('recebimento/parcela/<int:parcela>', RecebimentoParcela.as_view(), name='recebimento-parcela'),
    path('recebimento/parcela/negociacao/<int:parcela>', NegociacaoParcelaView.as_view(), name='negociacao-parcela'),
    path('recebimento/realizar-pagamento/<int:cliente>', RealizarPagamentoView.as_view(), name='realizar-pagamento')
]
