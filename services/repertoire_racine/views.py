import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def repertoire_racine(request):
    dropdown_parametre_generaux = 'True'
    repertoire_racine_active = 'True'
    header_title= "Répertoire racine"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'paramétrages',
            },
            {
                'name': 'répertoire racine',
            },
        ]
    return render(request, 'services/repertoire_racine/repertoire_racine.html', locals())

def list_repertoire_racine(request):
    get_data = requests.get(listeParametrages)
    data_list = get_data.json()
    return render(request, 'services/repertoire_racine/list_repertoire_racine.html', locals())

def edit_repertoire_racine(request, pk):
    get_famillerisk = requests.get(f"{listeParametrages}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('racine_rep')
         # Données à envoyer dans la requête POST
        data = {
                "racine_rep": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{listeParametrages}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/repertoire_racine/form_repertoire_racine.html", locals())
