# Generated by Django 2.0.2 on 2018-07-30 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medsis', '0006_auto_20180728_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentedesaude',
            options={'ordering': ['nome'], 'permissions': (('editar_agente', 'Pode editar Agente'),), 'verbose_name': 'Agente', 'verbose_name_plural': 'Agentes'},
        ),
    ]
