from django.http import HttpResponseRedirect
from .models import Item
from django.shortcuts import render
from .forms import ItemForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):

    itens = Item.objects.all()

    return render(request, 'item/index.html', {'itens': itens})

def cria(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/item/")
    else: 
        form = ItemForm()


    return render(request, 'item/cria.html', {'form': form})

def edita(request, id_item):

    item = Item.objects.get(id=id_item)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/item/")
    else:
        form = ItemForm(instance=item)
    return render(request, 'item/edita.html', {'form': form})

def deleta(request, id_item):
    item = Item.objects.get(id=id_item)
    item.delete()
    return HttpResponseRedirect("/item/")

def detalha(request, id_item):

    item = Item.objects.get(id=id_item)

    return render(request, 'item/detalhe.html', {'item': item})