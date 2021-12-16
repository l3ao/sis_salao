from django.urls import path
from .views import NotaServicoCreate, NotaServicoList, NotaServicoUpdate, NotaServicoDelete


urlpatterns = [
    path('', NotaServicoList.as_view(), name='notaservico-list'),
    path('add/', NotaServicoCreate.as_view(), name='notaservico-add'),
    path('notaservico/<int:pk>', NotaServicoUpdate.as_view(), name='notaservico-update'),
    path('notaservico/<int:pk>/delete', NotaServicoDelete.as_view(), name='notaservico-delete'),
]