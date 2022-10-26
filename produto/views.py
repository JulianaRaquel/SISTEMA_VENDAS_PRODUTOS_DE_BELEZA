from django.shortcuts import render
from .models import Produto, Marca

def home(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.all()
    marcas = Marca.objects.all()
    return render(request, 'home.html', {'produtos': produtos,
                                         'carrinho': len(request.session['carrinho']),
                                         'marcas': marcas})
def marca(request, id):
    produtos = Produto.objects.filter(marca_id=id)
    marcas = Marca.objects.all()
    return render(request, 'home.html', {'produtos': produtos, 'marcas': marcas})

def produto(request, id):
    marcas = Marca.objects.all()
    produto = Produto.objects.get(id=id)
    return render(request, 'produto.html', {'marcas': marcas, 'produto': produto})
