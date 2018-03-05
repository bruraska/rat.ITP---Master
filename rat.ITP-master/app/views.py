from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from models import *
from forms import *
from datetime import datetime
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def pagina_inicial(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Pagina inicial',
            'year':datetime.now().year,
        })
    )

def listar_aluno(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/aluno/listar_aluno.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de aluno',
            'alunos': Aluno.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_aluno(request, template_name='app/aluno/novo_aluno.html'):
    curso = Curso.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_aluno')
    return render(request, template_name, {'title':'Aluno', 'form':form, 'curso': curso})

def apagar_aluno(request, pk, template_name='app/aluno/confirmacao_apagar_aluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('listar_aluno')
    return render(request, template_name, {'object':aluno.nome_aluno})

def editar_aluno(request, pk, template_name='app/aluno/novo_aluno.html'):
    aluno= get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance = aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_aluno')
    return render(request, template_name, {'form':form})

def apagar_aluno(request, pk, template_name='app/aluno/confirmacao_apagar_aluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('listar_aluno')
    return render(request, template_name, {'object':aluno.nome_aluno})

