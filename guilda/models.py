from django.db import models

class Guilda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)

    class Meta:
        db_table = "Guilda_guilda"
        permissions = [
            ("detail_guilda", "Pode ver o detalhe da guilda"),
        ]

    def __str__(self):
        return self.nome
