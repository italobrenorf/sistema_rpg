from django.http import HttpResponseRedirect
from .models import Missao
from django.shortcuts import render
from .forms import MissaoForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):

    missoes = Missao.objects.all()

    return render(request, 'missao/index.html', {'missoes': missoes})

def cria(request):

    if request.method == "POST":
        form = MissaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/missao/")
    else: 
        form = MissaoForm()


    return render(request, 'missao/cria.html', {'form': form})

def edita(request, id_missao):

    missao = Missao.objects.get(id=id_missao)

    if request.method == "POST":
        form = MissaoForm(request.POST, instance=missao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/missao/")
    else:
        form = MissaoForm(instance=missao)
    return render(request, 'missao/edita.html', {'form': form})

def deleta(request, id_missao):
    missao = Missao.objects.get(id=id_missao)
    missao.delete()
    return HttpResponseRedirect("/missao/")

def detalha(request, id_missao):

    missao = Missao.objects.get(id=id_missao)

    return render(request, 'missao/detalhe.html', {'missao': missao})