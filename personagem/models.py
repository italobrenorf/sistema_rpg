from django.db import models
from guilda.models import Guilda
from usuario.models import Usuario
from item.models import Item


class Personagem(models.Model):
    TIPOS = [
        ('Personagem', 'Personagem'),
        ('Monstro', 'Monstro'),
        ('NPC', 'NPC'),
    ]

    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    nivel = models.IntegerField()
    hp = models.IntegerField()
    ouro = models.IntegerField()
    guilda = models.ForeignKey(Guilda, on_delete=models.SET_NULL, null=True)
    historia = models.CharField(max_length=500)
    criador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    inventario = models.ManyToManyField(Item, through='ItemPersonagem', related_name='personagens')

    class Meta:
        db_table = "Personagem_personagens"
        permissions = [
            ("detail_personagem", "Pode ver o detalhe do personagem"),
        ]

    def __str__(self):
        return self.nome


class ItemPersonagem(models.Model):
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    class Meta:
        db_table = "Personagem_itens"

    def __str__(self):
        return f"{self.personagem.nome} - {self.item.nome} (x{self.quantidade})"
