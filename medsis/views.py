from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse

from medsis.forms import AgenteDeSaudeForm
from medsis.models import AgenteDeSaude


def home(request):
    list_agentes = serialize("json", AgenteDeSaude.objects.all())
    return HttpResponse(list_agentes, content_type="application/json")


def agente_list(request):
    """"  
    list_agentes = serialize("json", AgenteDeSaude.objects.all())
    return HttpResponse(list_agentes, content_type="application/json")
    """
    template = 'agentes/index.html'
    list_agentes = AgenteDeSaude.objects.all()

    context = {
        'agentes': list_agentes,
    }

    return render(request, template, context)


@login_required
def agente_criar(request):
    template = 'agentes/agente_form.html'
    if request.method == 'POST':
        form = AgenteDeSaudeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agente cadastrado com Sucesso!')
            return HttpResponseRedirect(reverse('agentes'))
        else:
            print(form.errors)
    else:
        form = AgenteDeSaudeForm()

    return render(request, template, {'form': form})


def agente_edit(request, pk):
    template = 'agentes/agente_form.html'
    post = get_object_or_404(AgenteDeSaude, pk=pk)

    if request.method == 'POST':
        form = AgenteDeSaudeForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Agente atualizado com sucesso")
                return HttpResponseRedirect(reverse('agentes'))

        except Exception as e:
            messages.warning(request, 'Sua postagem não foi salva devido a um erro: {}'.format(e))

    else:
        form = AgenteDeSaudeForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


@user_passes_test(lambda u: u.is_staff)
def agente_delete(request, pk):
    template = 'agentes/confirme_delete.html'
    obj = get_object_or_404(AgenteDeSaude, pk=pk)
    if request.method == "POST":
        AgenteDeSaude.objects.filter(id=pk).delete()
        messages.success(request, "Deletado com sucesso!")
        return HttpResponseRedirect(reverse('agentes'))
    context = {
        "object": obj
    }
    return render(request, template, context)
