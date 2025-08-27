from django.http import HttpResponseRedirect
from .models import Item
from django.shortcuts import render
from .forms import ItemForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('item.view_item', raise_exception=True)
def index(request):

    itens = Item.objects.all()

    return render(request, 'item/index.html', {'itens': itens})

@login_required
@permission_required('item.add_item', raise_exception=True)
def cria(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/item/")
    else: 
        form = ItemForm()


    return render(request, 'item/cria.html', {'form': form})

@login_required
@permission_required('item.change_item', raise_exception=True)
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

@login_required
@permission_required('item.delete_item', raise_exception=True)
def deleta(request, id_item):
    item = Item.objects.get(id=id_item)
    item.delete()
    return HttpResponseRedirect("/item/")

@login_required
@permission_required('item.detail_item', raise_exception=True)
def detalha(request, id_item):

    item = Item.objects.get(id=id_item)

    return render(request, 'item/detalhe.html', {'item': item})