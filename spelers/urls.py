from django.urls import path
from . import views

urlpatterns = [
    path('speler/add/', views.newSpeler),
    path('editSpelers/<int:id>', views.editSpeler),
    path('deleteSpeler/', views.deleteSpeler),
    path('speler/<int:id>', views.spelerById),
    path('speler/', views.GegevensAlleSpelers),
    path('speler/names/', views.naamSpelers),
    path('addMatch/', views.newMatch),
    path('editMatch/<int:id>', views.editMatch),
    path('deleteMatch/', views.deleteMatch),
    path('matches/', views.allMatches),
    path('matchPunten/resultaat/<int:idSpeler>/<int:matchCode>', views.puntenIdCode),
    path('punten/<int:idSpeler>', views.puntenSpeler),
]