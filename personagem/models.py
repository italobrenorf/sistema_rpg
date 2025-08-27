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
    historia = models.TextField(blank=True)
    criador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True) #tirar duvida com carlos se tem como mudar automaticamente para o mestre e mudar o tipo dele para npc
    tipo = models.CharField(max_length=50, choices=TIPOS)
    inventario = models.ManyToManyField(Item, related_name='personagens')

    class Meta:
        db_table = "Personagem_personagens"
        permissions = [
            ("detail_personagem", "Pode ver o detalhe do personagem"),
        ]

    def __str__(self):
        return self.nome

