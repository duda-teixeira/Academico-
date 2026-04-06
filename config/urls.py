# urls.py principal do projeto
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', IndexView.as_view(), name='index'),
#     path('pessoas/', PessoasView.as_view(), name='pessoas'),
#     path('instituicoes/', InstituicaoEnsinoView.as_view(), name='instituicoes'),
#     path('cursos/', CursoView.as_view(), name='cursos'),
#     path('matriculas/', MatriculaView.as_view(), name='matriculas'),
#     path('disciplinas/', DisciplinaView.as_view(), name='disciplinas')
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoaView.as_view(), name='pessoas'),
    path('ocupacoes/', OcupacaoView.as_view(), name='ocupacoes'),
    path('instituicoes/', InstituicaoEnsinoView.as_view(), name='instituicoes'),
    path('cursos/', CursoView.as_view(), name='cursos'),
    path('matriculas/', MatriculaView.as_view(), name='matriculas'),
    path('disciplinas/', DisciplinaView.as_view(), name='disciplinas'),
    # Adicione as demais conforme necessário...
]