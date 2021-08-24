from django.contrib import admin
from .models import Produto, Categoria, UnidMedida

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(UnidMedida)