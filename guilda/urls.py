from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-guilda'),
path('<int:id_guilda>/', views.detalha, name='detalhe-guilda'),
path('add/', views.cria, name='add-guilda'),
path('edit/<int:id_guilda>/', views.edita, name='edit-guilda'),
path('delete/<int:id_guilda>/', views.deleta, name='delete-guilda'),
]