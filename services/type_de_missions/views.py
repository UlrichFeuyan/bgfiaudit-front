import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def type_de_missions(request):
    dropdown_parametre_generaux = 'True'
    dropdown_parametre_filiale = 'True'
    type_mission_active = 'True'
    header_title= "Type de  mission"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'paramétrages',
            },
            {
                'name': 'type de mission',
            },
        ]
    return render(request, 'services/type_de_missions/type_de_missions.html', locals())

def list_type_de_missions(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/type_de_missions/list_type_de_missions.html", locals())

def edit_type_de_missions(request, pk):
    get_famillerisk = requests.get(f"{typemission}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libtypemiss": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{typemission}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/type_de_missions/form_type_de_missions.html", locals())

def add_type_de_missions(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libtypemiss": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{typemission}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/type_de_missions/form_type_de_missions.html", locals())

def del_type_de_missions(request, pk):
    get_famillerisk = requests.get(f"{typemission}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{typemission}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/type_de_missions/del_type_de_missions.html", locals())
