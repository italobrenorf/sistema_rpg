from .models import Guilda
from django.forms import ModelForm

class GuildaForm(ModelForm):
    class Meta: 
        model =  Guilda
        fields = ['nome', 'descricao']