from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import (
    AvaliacaoTipo, Cidade, Turnos, Turma, AreaSaber, Ocupacao,
    Pessoa, InstituicaoEnsino, Curso, Disciplina, Matricula,
    Avaliacao, Frequencia, Ocorrencia, CursoDisciplina
)

# --- LISTAGENS SIMPLES (Sem chaves estrangeiras) ---

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class AvaliacaoTipoView(View):
    def get(self, request, *args, **kwargs):
        dados = AvaliacaoTipo.objects.all()
        return render(request, 'index.html', {'avaliacao_tipo': dados})

class TurnoView(View):
    def get(self, request, *args, **kwargs):
        dados = Turnos.objects.all()
        return render(request, 'index.html', {'turno': dados})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        dados = Turma.objects.all()
        return render(request, 'index.html', {'turma': dados})

class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        dados = AreaSaber.objects.all()
        return render(request, 'index.html', {'area_saber': dados})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        dados = Ocupacao.objects.all()
        return render(request, 'index.html', {'ocupacao': dados})

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        dados = Cidade.objects.all()
        return render(request, 'index.html', {'cidade': dados})

# --- LISTAGENS COM RELACIONAMENTOS (Usando select_related para performance) ---

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.select_related('cidade', 'ocupacao').all()
        return render(request, 'index.html', {'pessoa': pessoas})

class InstituicaoEnsinoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.select_related('cidade').all()
        return render(request, 'index.html', {'instituicao_ensino': instituicoes})

class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.select_related('area_saber', 'instituicao_ensino').all()
        return render(request, 'index.html', {'curso': cursos})

class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.select_related('area_saber').all()
        return render(request, 'index.html', {'disciplina': disciplinas})

class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.select_related('instituicao_ensino', 'curso', 'pessoa').all()
        return render(request, 'index.html', {'matricula': matriculas})

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.select_related('curso', 'disciplina', 'avaliacao_tipo').all()
        return render(request, 'index.html', {'avaliacao': avaliacoes})

class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.select_related('curso', 'disciplina', 'pessoa').all()
        return render(request, 'index.html', {'frequencia': frequencias})

class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.select_related('curso', 'disciplina', 'pessoa').all()
        return render(request, 'index.html', {'ocorrencia': ocorrencias})

class CursoDisciplinaView(View):
    def get(self, request, *args, **kwargs):
        relacoes = CursoDisciplina.objects.select_related('disciplina', 'curso').all()
        return render(request, 'index.html', {'curso_disciplina': relacoes})