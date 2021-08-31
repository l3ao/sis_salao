from django.urls import path
from .views import ProdutoList, ProdutoCreate, ProdutoUpdate, ProdutoDelete
from produtos import views


urlpatterns = [
    path('', ProdutoList.as_view(), name='produto-list'),
    path('add/', ProdutoCreate.as_view(), name='produto-add'),
    path('produto/<int:pk>', ProdutoUpdate.as_view(), name='produto-update'),
    path('produto/<int:pk>/delete', ProdutoDelete.as_view(), name='produto-delete'),
]