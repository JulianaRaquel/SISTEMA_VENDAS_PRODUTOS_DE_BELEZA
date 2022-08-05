from django.urls import path
from pedido.views import Pagar, FecharPedido, Detalhe

urlpatterns = [
    path('pagar/', Pagar.as_view(), name='pagar'),
    path('fecharpedido/', FecharPedido.as_view(), name='fecharpedido'),
    path('<slug>', Detalhe.as_view(), name='detalhe'),
]