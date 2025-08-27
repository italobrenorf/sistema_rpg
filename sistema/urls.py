from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda request: redirect('/conta/login/')),

    path('conta/', include('django.contrib.auth.urls')),

    path('personagem/', include('personagem.urls')),
    path('guilda/', include('guilda.urls')),
    path('item/', include('item.urls')),
    path('missao/', include('missao.urls')),
    path('usuario/', include('usuario.urls'))
]
