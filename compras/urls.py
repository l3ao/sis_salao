from django.urls import path
from compras import views

urlpatterns = [
    path('tipopagamento/', views.TipoPagamentoList.as_view(), name='tipopagamento-list'),
    path('tipopagamento/add/', views.TipoPagamentoCreate.as_view(), name='tipopagamento-add'),
    path('tipopagamento/<int:pk>/update', views.TipoPagamentoUpdate.as_view(), name='tipopagamento-update'),
    path('tipopagamento/<int:pk>/delete', views.TipoPagamentoDelete.as_view(), name='tipopagamento-delete'),
    path('', views.CompraList.as_view(), name='compra-list'),
    path('compra/add/', views.CompraCreate.as_view(), name='compra-add'),
    path('compra/<int:compra>/update', views.CompraUpdate.as_view(), name='compra-update'),
    path('compra/<int:compra>/delete', views.CompraDelete.as_view(), name='compra-delete'),
    path('compra/<int:compra>/item/add/', views.ItemCompraCreate.as_view(), name='itemcompra-add'),
    path('compra/item/<int:itemcompra>/update', views.ItemCompraUpdate.as_view(), name='itemcompra-update'),
    path('compra/item/<int:itemcompra>/delete', views.ItemCompraDelete.as_view(), name='itemcompra-delete'),
    path('compra/finalizarcompra/<int:compra>', views.FinalizarCompraView.as_view(), name='finalizar_compra'),
    path('pagamentos/', views.PagamentoList.as_view(), name='pagamento-list'),
    path('pagamentos/<int:compra>', views.PagamentoDetail.as_view(), name='pagamento-detail'),
    path('pagamentos/<int:parccompra>/pagar', views.PagarParcCompra.as_view(), name='pagar-parc_compra'),
]