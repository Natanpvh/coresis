# Generated by Django 2.0.2 on 2018-07-28 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medsis', '0005_auto_20180728_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentedesaude',
            options={'ordering': ['nome'], 'verbose_name': 'Agente', 'verbose_name_plural': 'Agentes'},
        ),
    ]
