from django.contrib import admin

# Register your models here.
from medsis.models import AgenteDeSaude, CadastroPaciente


class AgenteDeSaudeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rg')


admin.site.register(AgenteDeSaude, AgenteDeSaudeAdmin)


class CadastroPacienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(CadastroPaciente, CadastroPacienteAdmin)
