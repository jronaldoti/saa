from django.db import models
from locais.models import Local
from salas.models import Sala


class Translado(models.Model):
    local_novo = models.ForeignKey(Local,null=True,blank=True,on_delete=models.PROTECT)
    sala_novo = models.ForeignKey(Sala,null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.local_novo
