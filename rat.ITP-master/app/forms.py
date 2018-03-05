from django import forms
from django.forms import ModelForm
from models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class AlunoForm(forms.ModelForm):
    ra_aluno = forms.CharField(
    max_length=10,
    widget=forms.TextInput(
        attrs={
            'title': 'Ra',
            'type': 'number',
            'name': 'ra_aluno',
            'id': 'ra_aluno',
            'size': 10,
            'placeholder': 'Ra',
            'onkeypress' : 'validar(this); return numerico(event);'
        }
    )
)
    nome_aluno = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Nome',
            'type': 'text',
            'name': 'nome_aluno',
            'id': 'nome_aluno',
            'size': 15,
            'placeholder': 'Nome',
            'onkeypress': 'return somenteletraacento(event)'
        }
    )
)
    email_aluno = forms.CharField(
    max_length=50,
    widget=forms.TextInput(
        attrs={
            'title': 'Email',
            'type': 'email',
            'name': 'email_aluno',
            'id': 'email_aluno',
            'size': 15,
            'placeholder': 'Email',
        }
    )
)
    celular_aluno = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Celular',
            'type': 'number',
            'name': 'celular_aluno',
            'id': 'celular_aluno',
            'size': 10,
            'placeholder': 'Celular',
            'onkeypress' : 'validar(this); return numerico(event);'
        }
    )
)
    class Meta:
        model = Aluno
        fields = ['ra_aluno', 'nome_aluno', 'email_aluno', 'celular_aluno', 'sigla_curso']

