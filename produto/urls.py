from django.urls import path
from produto.views import home, produtoDetalhe, add_carrinho, rm_carrinho, carrinho

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('<slug>', produtoDetalhe.as_view(), name='detalhe'),
    path('add_carrinho/', add_carrinho.as_view(), name='add_carrinho'),
    path('rm_carrinho/', rm_carrinho.as_view(), name='rm_carrinho'),
    path('carrinho/', carrinho.as_view(), name='carrinho'),
]