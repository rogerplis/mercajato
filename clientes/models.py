from django.db import models

# Create your models here.
class Cliente(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.firstname

class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='carros', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)
    ano = models.IntegerField()
    lavagem = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)


