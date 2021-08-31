from django.urls import path
from tabelasbasicas import views

urlpatterns = [
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('categoria/add', views.CategoriaCreate.as_view(), name='categoria-add'),
    path('categoria/<int:pk>', views.CategoriaUpdate.as_view(), name='categoria-update'),
    path('categoria/<int:pk>/delete', views.CategoriaDelete.as_view(), name='categoria-delete'),
    path('unidmedidas/', views.UnidMedidaList.as_view(), name='unidmedida-list'),
    path('unidmedida/add', views.UnidMedidaCreate.as_view(), name='unidmedida-add'),
    path('unidmedida/<int:pk>', views.UnidMedidaUpdate.as_view(), name='unidmedida-update'),
    path('unidmedida/<int:pk>/delete', views.UnidMedidaDelete.as_view(), name='unidmedida-delete'),
    path('tipopagamento/', views.TipoPagamentoList.as_view(), name='tipopagamento-list'),
    path('tipopagamento/add/', views.TipoPagamentoCreate.as_view(), name='tipopagamento-add'),
    path('tipopagamento/<int:pk>/update', views.TipoPagamentoUpdate.as_view(), name='tipopagamento-update'),
    path('tipopagamento/<int:pk>/delete', views.TipoPagamentoDelete.as_view(), name='tipopagamento-delete'),
]