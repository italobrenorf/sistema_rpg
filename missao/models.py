from django.db import models
from item.models import Item  # relação com item futuramente
from personagem.models import Personagem

class Missao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    recompensa = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    personagens = models.ManyToManyField(Personagem, related_name='missoes')
    STATUS = [
        (True, 'Sim'),
        (False, 'Não'),
    ]
    concluida = models.BooleanField(choices=STATUS, default=False)

    class Meta:
        db_table = "Missao_missoes"
        permissions = [
            ("detail_missao", "Pode ver o detalhe da missao"),
        ]

    def __str__(self):
        return self.nome

