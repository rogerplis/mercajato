# Generated by Django 5.1.1 on 2024-10-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='valor',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]