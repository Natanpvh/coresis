from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate

from django.template.loader import render_to_string
from django.urls import reverse

from medsis.forms import AgenteDeSaudeForm, UsuarioForm
from medsis.models import AgenteDeSaude


def home(request):
    template = 'core/index.html'
    return render(request, template)


@login_required
@permission_required('medsis.lista_agente')
def agente_list(request):
    """ Lista os agentes de saude cadastrados """
    template = 'agentes/index.html'

    if 'q' in request.GET != False:

        lista_agentes = AgenteDeSaude.objects.all()

        busca = request.GET.get("q")

        query_list_busca = lista_agentes.filter(
            Q(rg=busca)|
            Q(nome__icontains=busca)
        )

        paginator = Paginator(query_list_busca, 3)
        page = request.GET.get('page', 1)
        try:
            agentes = paginator.page(page)
        except PageNotAnInteger:
            agentes = paginator.page(1)
        except EmptyPage:
            agentes = paginator.page(paginator.num_pages)

        context = {
            'paginator': paginator,
            'agentes': agentes,
        }

        return render(request, template, context)
    else:

        list_agentes = AgenteDeSaude.objects.all()
        paginator = Paginator(list_agentes, 3)
        page = request.GET.get('page', 1)
        try:
            agentes = paginator.page(page)
        except PageNotAnInteger:
            agentes = paginator.page(1)
        except EmptyPage:
            agentes = paginator.page(paginator.num_pages)

        context = {
            'paginator': paginator,
            'agentes': agentes,
        }

        return render(request, template, context)


@login_required
@permission_required('medsis.adicionar_agente', login_url='/accoubts/login/')
def agente_criar(request):
    """ Cadastra Agentes de Saúde """
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


@login_required
@permission_required('medsis.editar_agente', login_url='/accounts/login/')
def agente_edit(request, pk):
    """ Edita Agente de Saúde """
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


@login_required
@permission_required('medsis.deletar_agente', login_url='/accounts/login/')
def agente_delete(request, pk):
    """ Deleta Agente de Saúde """
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


def agente_visualisar(request, pk):
    """ Visualisa o Cadastro"""
    ver_agente = get_object_or_404(AgenteDeSaude, pk=pk)
    data = dict()
    if request.method == "GET":
        context = {"agente": ver_agente}
        data['html_agente'] = render_to_string('agentes/ver_agente.html', context, request=request)
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
        return redirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Nome de usuário ou senha')
    return render(request, template)


def usu_logout(request):
    auth.logout(request)
    return redirect('login_uso')
