from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    matricula = models.IntegerField()
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
