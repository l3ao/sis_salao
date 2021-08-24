from django.urls import path
from fornecedores import views

urlpatterns = [
    path('', views.FornecedorList.as_view(), name='fornecedor-list'),
    path('add/', views.FornecedorCreate.as_view(), name='fornecedor-add'),
    path('fornecedor/<int:pk>/update', views.FornecedorUpdate.as_view(), name='fornecedor-update'),
    path('fornecedor/<int:pk>/delete', views.FornecedorDelete.as_view(), name='fornecedor-delete'),
]