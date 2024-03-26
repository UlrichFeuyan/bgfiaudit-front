import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def mission(request):
    return render(request, 'services/mission/mission.html', locals())

def list_mission(request):
    get_data = requests.get(listeMission)
    data_list = get_data.json()
    return render(request, "services/mission/list_mission.html", locals())

def edit_mission(request, pk):
    get_famillerisk = requests.get(f"{listeMission}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        code_mission = request.POST.get('code_mission')
        intitule_mission = request.POST.get('intitule_mission')
        theme_mission = request.POST.get('theme_mission')
        debut_theo = request.POST.get('debut_theo')
        fin_theo = request.POST.get('fin_theo')
        statut_mission = request.POST.get('statut_mission')
        etat_mission = request.POST.get('etat_mission')
        # Données à envoyer dans la requête POST
        data = {
                "code_mission": code_mission,
                "intitule_mission": intitule_mission,
                "theme_mission": theme_mission,
                "debut_theo": debut_theo,
                "fin_theo": fin_theo,
                "statut_mission": statut_mission,
                "etat_mission": etat_mission,
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listeMission}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/mission/form_mission.html", locals())

def add_mission(request):
    if request.method == "POST":
        code_mission = request.POST.get('code_mission')
        intitule_mission = request.POST.get('intitule_mission')
        theme_mission = request.POST.get('theme_mission')
        debut_theo = request.POST.get('debut_theo')
        fin_theo = request.POST.get('fin_theo')
        statut_mission = request.POST.get('statut_mission')
        etat_mission = request.POST.get('etat_mission')
         # Données à envoyer dans la requête POST
        data = {
                "code_mission": code_mission,
                "intitule_mission": intitule_mission,
                "theme_mission": theme_mission,
                "debut_theo": debut_theo,
                "fin_theo": fin_theo,
                "statut_mission": statut_mission,
                "etat_mission": etat_mission,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listeMission}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/mission/form_mission.html", locals())

def del_mission(request, pk):
    get_famillerisk = requests.get(f"{listeMission}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listeMission}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/mission/del_mission.html", locals())
