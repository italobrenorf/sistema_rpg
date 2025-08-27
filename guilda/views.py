from django.http import HttpResponseRedirect
from .models import Guilda
from django.shortcuts import render
from .forms import GuildaForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('guilda.view_guilda', raise_exception=True)
def index(request):

    guildas = Guilda.objects.all()

    return render(request, 'guilda/index.html', {'guildas': guildas})

@login_required
@permission_required('guilda.add_guilda', raise_exception=True)
def cria(request):

    if request.method == "POST":
        form = GuildaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/guilda/")
    else: 
        form = GuildaForm()


    return render(request, 'guilda/cria.html', {'form': form})

@login_required
@permission_required('guilda.change_guilda', raise_exception=True)
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

@login_required
@permission_required('guilda.delete_guilda', raise_exception=True)
def deleta(request, id_guilda):
    guilda = Guilda.objects.get(id=id_guilda)
    guilda.delete()
    return HttpResponseRedirect("/guilda/")

@login_required
@permission_required('guilda.detail_guilda', raise_exception=True)
def detalha(request, id_guilda):

    guilda = Guilda.objects.get(id=id_guilda)

    return render(request, 'guilda/detalhe.html', {'guilda': guilda})