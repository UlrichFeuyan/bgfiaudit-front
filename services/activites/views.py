import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def activites(request):
    dropdown_activite_risque = 'True'
    activite_active = 'True'
    header_title= "Activités"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'activités et risques',
            },
            {
                'name': 'activités',
            },
        ]
    return render(request, 'services/activites/activites.html', locals())

def list_activites(request):
    get_data = requests.get(listeActivite)
    data_list = get_data.json()
    return render(request, "services/activites/list_activites.html", locals())

def edit_activites(request, pk):
    get_famillerisk = requests.get(f"{listeActivite}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        code_activite = request.POST.get('code_activite')
        # Données à envoyer dans la requête POST
        data = {
                "code_activite": code_activite,
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listeActivite}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/activites/form_activites.html", locals())

def add_activites(request):
    if request.method == "POST":
        code_activite = request.POST.get('code_activite')
        # Données à envoyer dans la requête POST
        data = {
                "code_activite": code_activite,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listeActivite}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/activites/form_activites.html", locals())

def del_activites(request, pk):
    get_famillerisk = requests.get(f"{listeActivite}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listeActivite}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/activites/del_activites.html", locals())
