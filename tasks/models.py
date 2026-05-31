from django.db import models
from django.conf import settings

from tasks.consts import OPCOES_PRIORIDADE, OPCOES_STATUS


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    data_hora_agendada = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=OPCOES_STATUS, default=1)
    prioridade = models.IntegerField(choices=OPCOES_PRIORIDADE, default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
