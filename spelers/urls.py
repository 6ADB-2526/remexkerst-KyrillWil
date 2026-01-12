from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('speler/add/', views.newSpeler),
    path('speler/<int:id>', views.spelerById),
    path('speler/', views.GegevensAlleSpelers),
    path('speler/names/', views.naamSpelers),
    path('addMatch/', views.newMatch),
    path('matches/', views.allMatches),
]