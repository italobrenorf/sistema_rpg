from django.http import HttpResponseRedirect
from .models import Guilda
from django.shortcuts import render
from .forms import GuildaForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):

    guildas = Guilda.objects.all()

    return render(request, 'guilda/index.html', {'guildas': guildas})

def cria(request):

    if request.method == "POST":
        form = GuildaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/guilda/")
    else: 
        form = GuildaForm()


    return render(request, 'guilda/cria.html', {'form': form})

def edita(request, id_guilda):

    guilda = Guilda.objects.get(id=id_guilda)

    if request.method == "POST":
        form = GuildaForm(request.POST, instance=guilda)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/guilda/")
    else:
        form = GuildaForm(instance=guilda)
    return render(request, 'guilda/edita.html', {'form': form})

def deleta(request, id_guilda):
    guilda = Guilda.objects.get(id=id_guilda)
    guilda.delete()
    return HttpResponseRedirect("/guilda/")

def detalha(request, id_guilda):

    guilda = Guilda.objects.get(id=id_guilda)

    return render(request, 'guilda/detalhe.html', {'guilda': guilda})