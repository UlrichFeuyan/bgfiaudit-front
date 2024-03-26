import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def processus(request):
    dropdown_parametre_filiale = 'True'
    processus_active = 'True'
    header_title= "Processus"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'paramétrages filiale',
            },
            {
                'name': 'processus',
            },
        ]
    return render(request, 'services/processus/processus.html', locals())

def list_processus(request):
    get_data = requests.get(listeProcessus)
    data_list = get_data.json()

    get_data_pole = requests.get(listePole)
    data_list_pole = get_data_pole.json()
    return render(request, "services/processus/list_processus.html", locals())

def edit_processus(request, pk):
    get_famillerisk = requests.get(f"{listeProcessus}{pk}")
    data = get_famillerisk.json()
    get_data_pole = requests.get(listePole)
    data_list_pole = get_data_pole.json()
    if request.method == "POST":
        libprocessus = request.POST.get('libprocessus')
        piloteprocessus = request.POST.get('piloteprocessus')
        idpole = request.POST.get('idpole')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "libprocessus": libprocessus,
                    "piloteprocessus": piloteprocessus,
                    "idpole": int(idpole),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.patch(f"{listeProcessus}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/processus/form_processus.html", locals())

def add_processus(request):
    get_data_pole = requests.get(listePole)
    data_list_pole = get_data_pole.json()
    if request.method == "POST":
        libprocessus = request.POST.get('libprocessus')
        piloteprocessus = request.POST.get('piloteprocessus')
        idpole = request.POST.get('idpole')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "libprocessus": libprocessus,
                    "piloteprocessus": piloteprocessus,
                    "idpole": int(idpole),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.post(f"{listeProcessus}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/processus/form_processus.html", locals())

def del_processus(request, pk):
    get_famillerisk = requests.get(f"{listeProcessus}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listeProcessus}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/processus/del_processus.html", locals())
