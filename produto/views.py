from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models

class home(ListView):
    model = models.Produto
    template_name = 'home.html'
    context_object_name = 'produtos'

class produtoDetalhe(DetailView):
    model = models.Produto
    template_name = 'detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class add_carrinho(View):
    pass

class rm_carrinho(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'rm_carrinho.html')

class carrinho(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'carrinho.html')


