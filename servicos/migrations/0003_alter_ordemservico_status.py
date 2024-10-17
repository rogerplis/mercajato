# Generated by Django 5.1.1 on 2024-10-09 22:30

import utils.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_orcamento_valor_alter_ordemservico_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='status',
            field=models.CharField(choices=utils.utils.StatusTypes.choices, default=utils.utils.StatusTypes['PENDENTE'], max_length=20),
        ),
    ]
