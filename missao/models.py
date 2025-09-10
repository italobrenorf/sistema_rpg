from django.db import models
from item.models import Item
from personagem.models import Personagem


class Missao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    recompensa = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    personagens = models.ManyToManyField(Personagem, through='MissaoPersonagem', related_name='missoes')

    class Meta:
        db_table = "Missao_missoes"
        permissions = [
            ("detail_missao", "Pode ver o detalhe da missao"),
        ]

    def __str__(self):
        return self.nome


class MissaoPersonagem(models.Model):
    missao = models.ForeignKey(Missao, on_delete=models.CASCADE)
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # se o personagem concluiu ou não

    class Meta:
        db_table = "Missao_personagens"

    def __str__(self):
        return f"{self.personagem.nome} - {self.missao.nome} ({'Concluída' if self.status else 'Em andamento'})"
