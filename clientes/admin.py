from django.contrib import admin
from .models import Cliente, Carro
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'cpf')
    search_fields = ('firstname', 'lastname', 'email', 'cpf')
    list_filter = ('firstname', 'lastname', 'email', 'cpf')
    ordering = ('firstname', 'lastname', 'email', 'cpf')
    list_per_page = 10


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'modelo', 'placa', 'ano', 'lavagem', 'consertos')
    search_fields = ('cliente', 'modelo', 'placa', 'ano', 'lavagem', 'consertos')
    list_filter = ('cliente', 'modelo', 'placa', 'ano', 'lavagem', 'consertos')
    ordering = ('cliente', 'modelo', 'placa', 'ano', 'lavagem', 'consertos')
    list_per_page = 10

