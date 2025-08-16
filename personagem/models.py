from django.db import models
# from guilda.models import Guilda

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
    # guilda
    historia = models.TextField(blank=True)
    # criador
    tipo = models.CharField(max_length=50, choices=TIPOS)


