from rest_framework import serializers
from .models import Cliente, Carro

class ClienteSerializer(serializers.ModelSerializer):
    carros = serializers.StringRelatedField(many=True)

    class Meta:
        extra_kwargs = {
            'cpf': {'write_only': True}
        }
        model = Cliente
        fields = [
            'id',
            'firstname',
            'lastname',
            'email',
            'cpf',
            'carros'
        ]

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'placa': {'write_only': True}
        }
        model = Carro
        fields = (
            'id',
            'cliente',
            'carro',
            'placa',
            'ano',
            'lavagem',
            'consertos'
        )
