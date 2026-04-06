from django.contrib import admin
from .models import *


#INLINES
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1 

class MatriculaInline(admin.TabularInline):
    model = Matricula
    # Substitua os nomes abaixo pelos nomes REAIS dos campos que existem na sua class Matricula no models.py
    fields = ['instituicao_ensino', 'curso', 'data_inicio', 'data_previsao_termino'] 
    extra = 1

class OcorrenciaInline(admin.StackedInline): 
    model = Ocorrencia
    extra = 0
    fields = ['data', 'descricao', 'disciplina', 'curso']

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber', 'instituicao_ensino')
    inlines = [CursoDisciplinaInline, AvaliacaoInline]

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade')
    inlines = [MatriculaInline, OcorrenciaInline]

@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]


admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(AreaSaber)
admin.site.register(Turma)
admin.site.register(Turnos)
admin.site.register(AvaliacaoTipo)
admin.site.register(Disciplina)
admin.site.register(Frequencia)