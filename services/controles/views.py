import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def controles(request):
    dropdown_activite_risque = 'True'
    controle_active = 'True'
    header_title= "Contrôles"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'activités et risques',
            },
            {
                'name': 'contrôles',
            },
        ]
    return render(request, 'services/controles/controles.html', locals())

def list_controles(request):
    get_data = requests.get(listcontroles)
    data_list = get_data.json()
    return render(request, "services/controles/list_controles.html", locals())

def edit_controles(request, pk):
    get_famillerisk = requests.get(f"{listcontroles}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        code_controles = request.POST.get('code_controles')
         # Données à envoyer dans la requête POST
        data = {
                "code_controles": code_controles
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listcontroles}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/controles/form_controles.html", locals())

def add_controles(request):
    if request.method == "POST":
        code_controles = request.POST.get('code_controles')
         # Données à envoyer dans la requête POST
        data = {
                "code_controles": code_controles
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listcontroles}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/controles/form_controles.html", locals())

def del_controles(request, pk):
    get_famillerisk = requests.get(f"{listcontroles}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listcontroles}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/controles/del_controles.html", locals())
