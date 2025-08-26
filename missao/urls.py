from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-missao'),
path('<int:id_missao>/', views.detalha, name='detalhe-missao'),
path('add/', views.cria, name='add-missao'),
path('edit/<int:id_missao>/', views.edita, name='edit-missao'),
path('delete/<int:id_missao>/', views.deleta, name='delete-missao'),
]