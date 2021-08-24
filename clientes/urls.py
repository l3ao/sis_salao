from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ClienteListView, ClienteCreate, ClienteUpdate, ClienteDelete


urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('add/', ClienteCreate.as_view(), name='cliente-add'),
    path('cliente/<int:pk>', ClienteUpdate.as_view(), name='cliente-update'),
    path('cliente/<int:pk>/delete', ClienteDelete.as_view(), name='cliente-delete'),
]