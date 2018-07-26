from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, PasswordInput
from django import forms
from django.contrib.auth.models import User

from .models import AgenteDeSaude


class AgenteDeSaudeForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nome'}
        )
    )
    rg = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-sm', 'placeholder': 'RG'}
        )
    )

    def adiciona_erro(self, message):
        self.full_clean()
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

    class Meta:
        model = AgenteDeSaude
        fields = ('__all__')


class UsuarioForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Senha deve ter números e letras'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirme a Senha'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 150}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 150, 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 150}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 150, 'required': 'required'}),
        }
