from django.db import models


class Item(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    valor = models.FloatField()
    descricao = models.TextField()

    class Meta:
        db_table = "Item_itens"
        permissions = [
            ("detail_item", "Pode ver o detalhe do item"),
        ]

    def __str__(self):
        return self.nome

