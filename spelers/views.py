from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import speler, match_punten
# Create your views here.

#spelers views:
#een nieuwe speler aanmaken
@csrf_exempt
def newSpeler(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    new = speler()
    new.naam = post_data["naam"]
    new.voornaam = post_data["voornaam"]
    new.email = post_data["email"]
    new.save()
    return JsonResponse(model_to_dict(new))

#een speler aanpassen aan de hand van een id
@csrf_exempt
def editSpeler(request, id):
    post_data =  json.loads(request.body.decode('utf-8'))
    editS = speler.objects.get(pk = id)
    editS.naam = post_data['naam']
    editS.voornaam = post_data['voornaam']
    editS.email = post_data['email']
    editS.save()
    return JsonResponse(model_to_dict(editS))

#een speler verwijderd aan de hand van een id
@csrf_exempt
def deleteSpeler(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    speler.objects.get(pk = post_data['id']).delete()
    return JsonResponse({"Status":"Speler succesvol verwijderd!"})

#een speler opzoeken aan de hand van een id, dit gebeurt in postman want anders is het niet veilig
def spelerById(request, id):
    idSpeler = speler.objects.get(pk = id)
    return JsonResponse(model_to_dict(idSpeler))

#alle spelers en de gegevens ervan tonen
def GegevensAlleSpelers(request):
    all = speler.objects.values()
    return JsonResponse(list(all), safe=False)

#alleeen de namen van alle spelers tonen
def naamSpelers(request):
    naam = speler.objects.values('naam', 'voornaam')
    return JsonResponse(list(naam), safe=False)

#match views:
#een nieuwe match aanmaken
@csrf_exempt
def newMatch(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    newM = match_punten()
    newM.nummerSpeler = post_data['nummerSpeler']
    newM.punten = post_data['punten']
    newM.matchCode = post_data['matchCode']
    newM.save()
    return JsonResponse(model_to_dict(newM))

#een match aanpassen aan de hand van een id
@csrf_exempt
def editMatch(request, id):
    post_data =  json.loads(request.body.decode('utf-8'))
    editM = match_punten.objects.get(pk = id)
    editM.nummerSpeler = post_data['nummerSpeler']
    editM.punten = post_data['punten']
    editM.matchCode = post_data['matchCode']
    editM.save()
    return JsonResponse(model_to_dict(editM))

#een match verwijderen aan de hand van een id, dit gebeurt in postman want anders is het niet veilig
@csrf_exempt
def deleteMatch(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    match_punten.objects.get(pk = post_data['id']).delete()
    return JsonResponse({"Status":"Match succesvol verwijderd!"})

#alle matches tonen
def allMatches(request):
    all = match_punten.objects.values()
    return JsonResponse(list(all), safe=False)

#de punten van een specieke match van een specifieke speler tonen
def puntenIdCode(request, idSpeler, matchCode):
    idCode = match_punten.objects.filter(nummerSpeler = idSpeler).filter(matchCode = matchCode).values('punten')
    return JsonResponse(list(idCode), safe=False)

#de alle punten van een specifieke speler tonen
def puntenSpeler(request, idSpeler):
    spelerId = match_punten.objects.filter(nummerSpeler = idSpeler).values('punten')
    return JsonResponse(list(spelerId), safe=False)

  