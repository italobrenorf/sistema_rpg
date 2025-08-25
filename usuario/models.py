from django.db import models

class Usuario(models.Model):
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, blank=True, null=True )

    def __str__(self):
        return self.nome
