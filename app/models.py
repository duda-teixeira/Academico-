from django.db import models

# Create your models here.

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Gerenciar ocupação de pessoas")