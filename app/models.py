from django.db import models

# Create your models here.

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupação")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"
        
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área") 
    def __str__(self):
        return f"{self.nome}"  
    class Meta:
        verbose_name = "AreaSaber"
        verbose_name_plural = "AreasSaber"
        
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Nome da Turma")
    def __str__(self):
       return f"{self.nome}"
    class Meta:
       verbose_name = "Turma"
       verbose_name_plural = "Turmas"
       
class Turnos(models.Model):
    nome = models.CharField(max_length=100, verbose_name ="Nome dos Turnos")
    def __str__(self):
        return f"{self.nome}"    
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Nome da Cidade")
    uf = models.CharField(max_length=100, verbose_name = "UF")          
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Tipo da Avaliação")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "AvaliacaoTipo"
        verbose_name_plural = "AvaliacoesTipos"
        
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, default=1, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, default=1, verbose_name="Nome do Pai da pessoa")
    mae = models.CharField(max_length=100, default=1, verbose_name="Nome da Mae da pessoa")
    cpf = models.CharField(max_length=100, default=1, verbose_name="CPF da Pessoa")
    data_nasc = models.DateField(max_length=100, default=1, verbose_name="Data de Nascimento da pessoa")
    email = models.CharField(max_length=100, default=1, verbose_name="Email da Pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1, verbose_name="Cidade da Pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, default=1, verbose_name="Ocupação da Pessoa")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Nome da Instituição")
    site = models.CharField(max_length=100, verbose_name = "Site da Instituição")
    telefone = models.CharField(max_length=100, )
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name = "Cidade da Instituição")  
    def __str__(self):
        return f"{self.nome}, {self.site}, {self.telefone}"
    class Meta:
        verbose_name = "InstituicaoEnsino"
        verbose_name_plural = "InstituicoesEnsino"
        
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cursos")
    carga_horaria_total = models.CharField(max_length=100, verbose_name="Carga Horaria Total")
    duracao_meses = models.CharField(max_length=100, verbose_name="Duração em Meses") 
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Area do Curso")  
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição do Curso")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Area da Disciplina")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"
        
class Matricula(models.Model):
    data_inicio = models.DateField(max_length=100, verbose_name="Data de Início da Matrícula")
    data_previsao_termino = models.DateField(max_length=100, verbose_name="Data de Previsão do Término do Curso")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso da Matricula")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa Matriculada")
    def __str__(self):
        return f"{self.pessoa}, {self.curso}"
    class Meta:
        verbose_name="Matricula"
        verbose_name_plural = "Matriculas"
        
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da Avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso da Avaliação")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina da Avaliação")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo da Avaliação")
    def __str__(self):
        return f"{self.curso}, {self.descricao}"
    class Meta:
        verbose_name="Avaliacao"
        verbose_name_plural="Avaliacoes"
        
class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default='1', verbose_name="Aluno")  
    curso = models.CharField(max_length=100, default='1', verbose_name="Curso")
    numero_faltas = models.CharField(max_length=100, default='1', verbose_name="Numero de Faltas")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, default='1', verbose_name="Disciplina da Ausência/Presença")
    def __str__(self):
        return f"{self.pessoa}, {self.curso}, {self.disciplina}" 
    class Meta:
        verbose_name="Frequencia"
        verbose_name_plural="Frequencias"    
        
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descricão da Ocorrência")
    data = models.DateField(max_length=100, verbose_name="Data da Ocorrência") 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso da Ocorrência")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina em que aconteceu a Ocorrência")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa da Ocorrência") 
    def __str__(self):
        return f"{self.pessoa}, {self.data}"
    class Meta:
        verbose_name="Ocorrencia"
        verbose_name_plural = "Ocorrencias"
        
class CursoDisciplina(models.Model):
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga Horária da Disciplina")
    periodo = models.CharField(max_length=100, verbose_name="Período do Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina do Curso") 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")                 
    def __str__(self):
        return f"{self.curso}, {self.disciplina}"
    class Meta:
        verbose_name="CursoDisciplina"
        verbose_name_plural="CursosDisciplinas"
    
            
            
            