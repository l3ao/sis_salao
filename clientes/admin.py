from django.contrib import admin
from .models import Cliente


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'endereco')


admin.site.register(Cliente, ClienteAdmin)