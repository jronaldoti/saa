from django.db import models


class Local(models.Model):
        nome = models.CharField(max_length=40)
        rua = models.CharField(max_length=40)
        numero = models.IntegerField()
        bairro = models.CharField(max_length=30)

        def __str__(self):
            return self.nome





