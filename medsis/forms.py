from django import forms
from django.core.exceptions import ValidationError

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
