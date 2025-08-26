from .models import Item
from django.forms import ModelForm

class ItemForm(ModelForm):
    class Meta: 
        model =  Item
        fields = ['nome', 'tipo', 'valor', 'descricao']