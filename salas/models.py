from django.db import models
from locais.models import Local


class Sala(models.Model):
    local = models.ForeignKey(Local,null=True,blank=True,on_delete=models.PROTECT)
    nome = models.CharField(max_length=40)
    numero = models.IntegerField()

    def __str__(self):
        return self.nome