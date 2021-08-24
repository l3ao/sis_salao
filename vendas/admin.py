from django.contrib import admin
from .models import Venda, ItemDaVenda, ParcelaVenda

class ItemDaVendaInline(admin.TabularInline):
    model = ItemDaVenda


class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemDaVendaInline]

# Register your models here.
admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDaVenda)
admin.site.register(ParcelaVenda)
