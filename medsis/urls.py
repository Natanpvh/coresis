"""coresis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    #login
    path('accounts/login/', views.usu_login, name='login_uso'),
    path('logout/', views.usu_logout, name='usu_logout'),
    #AGENTES DE SAUDE
    path('', views.home, name='index'),
    path('agentes/', views.agente_list, name='agentes'),
    path('agentes/criar/', views.agente_criar, name='criar_agente'),
    path('agente/edit/<int:pk>/', views.agente_edit, name='edit_agente'),
    path('agente/delet/<int:pk>/', views.agente_delete, name='agente_delete'),

    #Cadastro de usuarios
    path('cadastro/', views.cadastro_usuario, name='cadastro_usu')
]
