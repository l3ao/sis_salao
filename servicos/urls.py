from django.urls import path
from .views import ServicoList, ServicoCreate, ServicoUpdate, ServicoDelete


urlpatterns = [
    path('', ServicoList.as_view(), name='servico-list'),
    path('add/', ServicoCreate.as_view(), name='servico-add'),
    path('servico/<int:pk>/', ServicoUpdate.as_view(), name='servico-update'),
    path('servico/<int:pk>/delete', ServicoDelete.as_view(), name='servico-delete'),
]
