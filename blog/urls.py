from django.urls import path
from . import views

urlpatterns = [
    path('konoha', views.konoha, name='konoha'),
    path('marais', views.marais, name='marais'),
    path('zone51', views.zone, name='zone51'),
    path('champ_de_bataille', views.bataille, name='champ_de_bataille'),
    path('chasse', views.chasse, name='terrain_de_chasse'),
    path('psy', views.psy, name='cellule_psy'),
    path('', views.equipement, name='worldMap'),
    path('character/<str:id_character>/?<str:message>', views.formulaire, name='formulaire_mes'),
    path('character/<str:id_character>/', views.formulaire, name='formulaire'),

]