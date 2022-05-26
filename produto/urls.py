from django.urls import path
from .views import listar, novo, alterar, deletar

app_name = 'produto'

urlpatterns = [
    path('listar/', listar, name='listar'),
    path('novo/', novo, name='novo'),
    path('alterar/<int:pk>/', alterar, name='alterar'),
    path('deletar/<int:pk>/', deletar, name='deletar')
]