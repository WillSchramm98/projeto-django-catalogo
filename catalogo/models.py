from django.db import models


class Tema(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField()

    def __str__(self):
        return self.titulo


class Recurso(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)
    link = models.URLField()
    gratuito = models.BooleanField(default=True)
    prestigio = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
