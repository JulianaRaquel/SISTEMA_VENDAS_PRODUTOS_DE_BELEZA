from django.contrib import admin
from produto.models import Categoria, Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('icone', 'nome', 'categoria', 'preco', 'ativo')
    list_editable = ('preco', 'ativo')

admin.site.register(Categoria)
