# Generated by Django 2.0.2 on 2018-07-31 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medsis', '0008_auto_20180730_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentedesaude',
            options={'ordering': ['nome'], 'permissions': (('lista_agente', 'Lista Agentes'), ('adicionar_agente', 'Pode Adicionar Agente'), ('editar_agente', 'Pode editar Agente'), ('deletar_agente', 'Pode deletar Agente'), ('ver_agente', 'Pode visualizar Agente')), 'verbose_name': 'Agente', 'verbose_name_plural': 'Agentes'},
        ),
    ]
