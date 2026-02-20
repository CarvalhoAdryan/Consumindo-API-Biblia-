from django.urls import path
from . import views

urlpatterns = [
    path('<str:versao>/<str:livro_abrev>/<int:capitulo>',views.Index, name='index'),
    path('lista/',views.Books, name='livros')
    ]
