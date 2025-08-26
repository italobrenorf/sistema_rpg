from django.http import HttpResponseRedirect
from .models import Usuario
from django.shortcuts import render
from .forms import UsuarioForm, UsuarioEditForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):

    usuarios = Usuario.objects.all()

    return render(request, 'usuario/index.html', {'usuarios': usuarios})

def cria(request):

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/usuario/")
    else: 
        form = UsuarioForm()


    return render(request, 'usuario/cria.html', {'form': form})

def edita(request, id_usuario):

    usuario = Usuario.objects.get(id=id_usuario)

    if request.method == "POST":
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/usuario/")
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'usuario/edita.html', {'form': form})

def deleta(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return HttpResponseRedirect("/usuario/")

def detalha(request, id_usuario):

    usuario = Usuario.objects.get(id=id_usuario)

    return render(request, 'usuario/detalhe.html', {'usuario': usuario})