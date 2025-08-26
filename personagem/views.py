from django.http import HttpResponseRedirect
from .models import Personagem
from django.shortcuts import render
from .forms import PersonagemForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):

    personagens = Personagem.objects.all()

    return render(request, 'personagem/index.html', {'personagens': personagens})

def cria(request):

    if request.method == "POST":
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/personagem/")
    else: 
        form = PersonagemForm()


    return render(request, 'personagem/cria.html', {'form': form})

def edita(request, id_personagem):

    personagem = Personagem.objects.get(id=id_personagem)

    if request.method == "POST":
        form = PersonagemForm(request.POST, instance=personagem)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/personagem/")
    else:
        form = PersonagemForm(instance=personagem)
    return render(request, 'personagem/edita.html', {'form': form})

def deleta(request, id_personagem):
    personagem = Personagem.objects.get(id=id_personagem)
    personagem.delete()
    return HttpResponseRedirect("/personagem/")

def detalha(request, id_personagem):

    personagem = Personagem.objects.get(id=id_personagem)

    return render(request, 'personagem/detalhe.html', {'personagem': personagem})