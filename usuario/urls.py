from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-usuario'),
path('<int:id_usuario>/', views.detalha, name='detalhe-usuario'),
path('add/', views.cria, name='add-usuario'),
path('edit/<int:id_usuario>/', views.edita, name='edit-usuario'),
path('delete/<int:id_usuario>/', views.deleta, name='delete-usuario'),
]