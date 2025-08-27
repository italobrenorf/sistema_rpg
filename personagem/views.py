from django.http import HttpResponseRedirect
from .models import Personagem
from django.shortcuts import render
from .forms import PersonagemForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('personagem.view_personagem', raise_exception=True)
def index(request):

    personagens = Personagem.objects.all()

    return render(request, 'personagem/index.html', {'personagens': personagens})

@login_required
@permission_required('personagem.add_personagem', raise_exception=True)
def cria(request):

    if request.method == "POST":
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/personagem/")
    else: 
        form = PersonagemForm()


    return render(request, 'personagem/cria.html', {'form': form})

@login_required
@permission_required('personagem.change_personagem', raise_exception=True)
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

@login_required
@permission_required('personagem.delete_personagem', raise_exception=True)
def deleta(request, id_personagem):
    personagem = Personagem.objects.get(id=id_personagem)
    personagem.delete()
    return HttpResponseRedirect("/personagem/")

@login_required
@permission_required('personagem.detail_personagem', raise_exception=True)
def detalha(request, id_personagem):

    personagem = Personagem.objects.get(id=id_personagem)

    return render(request, 'personagem/detalhe.html', {'personagem': personagem})