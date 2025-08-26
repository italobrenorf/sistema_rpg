from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('personagem/', include('personagem.urls')),
    path('guilda/', include('guilda.urls')),
    path('item/', include('item.urls')),
    path('missao/', include('missao.urls')),
    path('usuario/', include('usuario.urls'))
]
