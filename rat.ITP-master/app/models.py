from django.db import models
from django.core.urlresolvers import reverse

class Aluno(models.Model):
    ra_aluno = models.CharField(max_length=10)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(max_length=50)
    celular_aluno = models.CharField(max_length=15)
    sigla_curso = models.CharField(max_length=5)


