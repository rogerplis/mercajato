from django.db import models

from clientes.models import Carro, Cliente
from utils.utils import StatusTypes

# Create your models here.
class Servico(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return self.tipo

class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    valor = models.FloatField(default=0.0)
    data = models.DateField(auto_now_add=True)
    tempoExecucao = models.IntegerField()


    def __str__(self):
        return self.carro.placa

class ItemOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento,related_name='orcamentos', on_delete=models.CASCADE)
    tipoServico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao


class OrdemServico(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    dataInicio = models.DateField(auto_now_add=True)
    dataFim = models.DateField()
    descricao = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=StatusTypes.choices, default=StatusTypes.PENDENTE)

    def __str__(self):
        return self.descricao

    def get_servico_type_label(self):
        return StatusTypes(self.status).name.title()