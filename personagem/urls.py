from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-personagem'),
path('<int:id_personagem>/', views.detalha, name='detalhe-personagem'),
path('add/', views.cria, name='add-personagem'),
path('edit/<int:id_personagem>/', views.edita, name='edit-personagem'),
path('delete/<int:id_personagem>/', views.deleta, name='delete-personagem'),
]