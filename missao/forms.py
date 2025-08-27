from .models import Missao
from django.forms import ModelForm

class MissaoForm(ModelForm):
    class Meta: 
        model =  Missao
        fields = ['nome', 'descricao', 'recompensa']

class MissaoEditForm(ModelForm):
    class Meta: 
        model =  Missao
        fields = ['nome', 'descricao', 'recompensa', 'concluida', 'personagens']