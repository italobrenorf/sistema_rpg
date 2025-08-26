from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'data_nascimento', 'telefone']

class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'data_nascimento', 'telefone']
