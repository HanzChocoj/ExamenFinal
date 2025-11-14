from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_categorias, name='listar_categorias'),
    path('crear/', views.crear_categoria, name='crear_categoria'),
    path('editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
]
