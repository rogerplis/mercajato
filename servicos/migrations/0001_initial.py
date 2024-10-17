# Generated by Django 5.1.1 on 2024-10-09 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('data', models.DateField(auto_now_add=True)),
                ('tempoExecucao', models.IntegerField()),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.carro')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateField(auto_now_add=True)),
                ('dataFim', models.DateField()),
                ('descricao', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.orcamento')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('valor', models.FloatField()),
                ('aprovado', models.BooleanField(default=False)),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.orcamento')),
                ('tipoServico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.servico')),
            ],
        ),
    ]