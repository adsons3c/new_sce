from django.urls import path, include
from .views import Create_Equipamento, create_manutencao


app_name = 'sce'
urlpatterns = [
    # path('home/', Home.as_view(), name='home'),
    path('home', Create_Equipamento.as_view(), name='addequipamento'),
    path('manutencao/<int:pk>', create_manutencao, name="manutencao")

]
