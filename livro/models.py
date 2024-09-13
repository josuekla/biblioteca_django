from django.db import models
from datetime import date

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(default = date.today)
    emprestrado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True) #Aqui é o nome da pessoa que para quem o livro foi emprestado
    data_emprestimo = models.DateField(blank=True) # O dia que o livro foi emprestado
    tempo_duração = models.DateField(blank=True)

    class Meta:
        verbose_name = 'livro'

    def __str__(self):
        return self.nome
    