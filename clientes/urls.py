from django.urls import path
from .views import ClienteListView, ClienteCreate, ClienteUpdate, ClienteDelete, IndexView


urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('add/', ClienteCreate.as_view(), name='cliente-add'),
    path('cliente/<int:pk>', ClienteUpdate.as_view(), name='cliente-update'),
    path('cliente/<int:pk>/delete', ClienteDelete.as_view(), name='cliente-delete'),
    path('cliente_index/', IndexView.as_view(), name='cliente-index'),
]