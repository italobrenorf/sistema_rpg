from django.db import models
from item.models import Item  # relação com item futuramente

class Missao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    recompensa = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

