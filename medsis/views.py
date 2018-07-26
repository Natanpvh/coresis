from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required, permission_required
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse

from medsis.forms import AgenteDeSaudeForm, UsuarioForm
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


"""
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
"""


def agente_criar(request):
    data = dict()
    if request.method == 'POST':
        form = AgenteDeSaudeForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = AgenteDeSaudeForm()

    context = {'form': form}
    data['html_form'] = render_to_string('agentes/agente_form.html',
                                         context,
                                         request=request,

                                         )
    return JsonResponse(data)


def agente_edit(request, pk):
    data = dict()
    agente = get_object_or_404(AgenteDeSaude, pk=pk)

    if request.method == 'POST':
        form = AgenteDeSaudeForm(request.POST, instance=agente)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    else:
        form = AgenteDeSaudeForm(instance=agente)
    context = {'form': form}
    data['html_form'] = render_to_string('agentes/agente-form-update.html',
                                         context,
                                         request=request,

                                         )
    return JsonResponse(data)


def agente_delete(request, pk):
    agente_d = get_object_or_404(AgenteDeSaude, pk=pk)
    data = dict()
    if request.method == "POST":
        agente_d.delete()
        data['form_is_valid'] = True
    else:
        context = {"agente": agente_d}
        data['html_form'] = render_to_string('agentes/confirme_delete.html',
                                             context,
                                             request=request
                                             )
    return JsonResponse(data)


def cadastro_usuario(request):
    form = UsuarioForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario cadastrado com Sucesso!')
            return HttpResponseRedirect(reverse('cadastro_usu'))
    return render(request, 'template_login/cadastro.html', context)


def usu_login(request):
    template = 'template_login/login.html'
    if request.user.is_authenticated == True:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, template)


def usu_logout(request):
    auth.logout(request)
    return redirect('login_uso')
