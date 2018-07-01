from django.db import models


class Patrimonio(models.Model):
        tombo = models.CharField(max_length=40)
        nome = models.CharField(max_length=40)
        especificacao = models.CharField(max_length=40)

        def __str__(self):
            return self.nome