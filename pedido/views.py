from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class Pagar(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'pagar.html')

class FecharPedido(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fecharpedido.html')

class Detalhe(View):
    pass
