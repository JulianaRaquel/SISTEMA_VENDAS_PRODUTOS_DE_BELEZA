from django.contrib import admin
from produto.models import Categoria, Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('icone', 'nome', 'categoria', 'preco', 'ativo')
    list_editable = ('preco', 'ativo')

"""class VariacaoInline(admin, TabularInline):
    model = models.Variacao"""

admin.site.register(Categoria)
