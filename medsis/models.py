from django.db import models


# Create your models here.
class AgenteDeSaude(models.Model):
    nome = models.CharField(u'Nome:', max_length=150)
    rg = models.CharField(u'RG:', max_length=15, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = "Agente"
        verbose_name_plural = "Agentes"
        permissions =(
            ('lista_agente', 'Lista Agentes'),
            ('adicionar_agente', 'Pode Adicionar Agente'),
            ('editar_agente', 'Pode editar Agente'),
            ('deletar_agente', 'Pode deletar Agente'),
            ('ver_agente', 'Pode visualizar Agente'),
        )

    def __str__(self):
        return self.nome


# Model para cadastro de pacientes.
class CadastroPaciente(models.Model):
    SEXO_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMININO'),
    )
    RACA_CHOICES = (
        ('B', 'Branca'),
        ('N', 'Negra'),
        ('P', 'Parda'),
    )
    nome = models.CharField(u'Nome:', max_length=150)
    idade = models.IntegerField(u'Idade:')
    datade_nascimento = models.DateField(u'Data de Nascimento:')
    rg = models.IntegerField(u'RG:', unique=True)
    ssp = models.CharField(u'SS/P:', max_length=4)
    cpf = models.CharField(u'CPF:', max_length=11, unique=True)
    cartao_sus = models.CharField(u'Cartão do SUS:', max_length=20)
    sexo = models.CharField(u'Sexo:', max_length=1, choices=SEXO_CHOICES)
    raca = models.CharField(u'Raça:', max_length=1, choices=RACA_CHOICES)
    proficao = models.CharField(u'Profissão/escolaridade:', max_length=100)
    endereco = models.CharField(u'Endereço:', max_length=150)
    numero = models.IntegerField(u'Numero:')
    bairro = models.CharField(u'Bairro:', max_length=150)
    fonefixo = models.CharField(u'Telefone Fixo:', max_length=10)
    celular = models.CharField(u'Celular:', max_length=11)
    procedencia = models.CharField(u'Procedencia:', max_length=155)
    agente_saude = models.ForeignKey(AgenteDeSaude, verbose_name='Agente de Saude:', on_delete=models.SET_NULL,
                                     null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['date_created']
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nome
