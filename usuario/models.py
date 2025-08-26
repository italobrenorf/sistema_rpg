from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, blank=True, null=True )

    class Meta:
        db_table = "Usuario_usuarios"
        permissions = [
            ("detail_usuario", "Pode ver o detalhe do usuario"),
        ]

    def __str__(self):
        return self.nome
