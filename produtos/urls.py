from django.urls import path
from .views import ProdutoList, ProdutoCreate, ProdutoUpdate, ProdutoDelete
from produtos import views


urlpatterns = [
    path('', ProdutoList.as_view(), name='produto-list'),
    path('add/', ProdutoCreate.as_view(), name='produto-add'),
    path('produto/<int:pk>', ProdutoUpdate.as_view(), name='produto-update'),
    path('produto/<int:pk>/delete', ProdutoDelete.as_view(), name='produto-delete'),
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('categoria/add', views.CategoriaCreate.as_view(), name='categoria-add'),
    path('categoria/<int:pk>', views.CategoriaUpdate.as_view(), name='categoria-update'),
    path('categoria/<int:pk>/delete', views.CategoriaDelete.as_view(), name='categoria-delete'),
    path('unidmedidas/', views.UnidMedidaList.as_view(), name='unidmedida-list'),
    path('unidmedida/add', views.UnidMedidaCreate.as_view(), name='unidmedida-add'),
    path('unidmedida/<int:pk>', views.UnidMedidaUpdate.as_view(), name='unidmedida-update'),
    path('unidmedida/<int:pk>/delete', views.UnidMedidaDelete.as_view(), name='unidmedida-delete'),
]