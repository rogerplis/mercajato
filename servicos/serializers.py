from rest_framework import serializers
from .models import Servico, Orcamento, ItemOrcamento, OrdemServico


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = (
            'id',
            'tipo',
            'valor'
        )
class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamento
        fields = (
            'id',
            'cliente',
            'carro',
            'valor',
            'data',
            'tempoExecucao'
        )

class ItemOrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrcamento
        fields = (
            'id',
            'orcamento',
            'tipoServico',
            'descricao',
            'quantidade',
            'valor',
            'aprovado'
        )

class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = (
            'id',
            'orcamento',
            'dataInicio',
            'dataFim',
            'descricao',
            'status'
        )
        
