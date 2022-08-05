from django.contrib import admin
from pedido.models import Pedido, Status, ItemPedido
from . import models

class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Status)
admin.site.register(ItemPedido)
