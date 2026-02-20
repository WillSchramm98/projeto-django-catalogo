from django.db import models


class Questao(models.Model):
    descricao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao


class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.descricao
