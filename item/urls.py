from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-item'),
path('<int:id_item>/', views.detalha, name='detalhe-item'),
path('add/', views.cria, name='add-item'),
path('edit/<int:id_item>/', views.edita, name='edit-item'),
path('delete/<int:id_item>/', views.deleta, name='delete-item'),
]