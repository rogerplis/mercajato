from django.contrib import admin
from .models import Servico, Orcamento, ItemOrcamento, OrdemServico
# Register your models here.
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'valor')
    search_fields = ('tipo', 'valor')
    list_filter = ('tipo', 'valor')
    ordering = ('tipo', 'valor')
    list_per_page = 10

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carro', 'valor', 'data', 'tempoExecucao')
    search_fields = ('cliente', 'carro', 'valor', 'data', 'tempoExecucao')
    list_filter = ('cliente', 'carro', 'valor', 'data', 'tempoExecucao')
    ordering = ('cliente', 'carro', 'valor', 'data', 'tempoExecucao')
    list_per_page = 10

@admin.register(ItemOrcamento)
class ItemOrcamentoAdmin(admin.ModelAdmin):
    list_display = ('orcamento', 'tipoServico', 'descricao', 'quantidade', 'valor', 'aprovado')
    search_fields = ('orcamento', 'tipoServico', 'descricao', 'quantidade', 'valor', 'aprovado')
    list_filter = ('orcamento', 'tipoServico', 'descricao', 'quantidade', 'valor', 'aprovado')
    ordering = ('orcamento', 'tipoServico', 'descricao', 'quantidade', 'valor', 'aprovado')
    list_per_page = 10

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('orcamento', 'dataInicio', 'dataFim', 'descricao', 'status')
    search_fields = ('orcamento', 'dataInicio', 'dataFim', 'descricao', 'status')
    list_filter = ('orcamento', 'dataInicio', 'dataFim', 'descricao', 'status')
    ordering = ('orcamento', 'dataInicio', 'dataFim', 'descricao', 'status')
    list_per_page = 10
