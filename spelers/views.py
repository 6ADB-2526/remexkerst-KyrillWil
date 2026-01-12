from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import speler, match_punten
# Create your views here.

def test(request):
   return HttpResponse('Test')

#spelers
@csrf_exempt
def newSpeler(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    new = speler()
    new.naam = post_data["naam"]
    new.voornaam = post_data["voornaam"]
    new.email = post_data["email"]
    new.save()
    return JsonResponse(model_to_dict(new))

def spelerById(request, id):
    idSpeler = speler.objects.get(pk = id)
    return JsonResponse(model_to_dict(idSpeler))

def GegevensAlleSpelers(request):
    all = speler.objects.values()
    return JsonResponse(list(all), safe=False)

def naamSpelers(request):
    naam = speler.objects.values('naam', 'voornaam')
    return JsonResponse(list(naam), safe=False)

#match
@csrf_exempt
def newMatch(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    newM = match_punten()
    newM.nummerSpeler = post_data['nummerSpeler']
    newM.punten = post_data['punten']
    newM.matchCode = post_data['matchCode']
    newM.save()
    return JsonResponse(model_to_dict(newM))

def allMatches(request):
    all = match_punten.objects.values()
    return JsonResponse(list(all), safe=False)
  