import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def risques(request):
    dropdown_activite_risque = 'True'
    risque_active = 'True'
    header_title= "Risques"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'activités et risques',
            },
            {
                'name': 'risques',
            },
        ]
    return render(request, 'services/risques/risques.html', locals())

def list_risques(request):
    get_data = requests.get(listerisque)
    data_list = get_data.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    return render(request, "services/risques/list_risques.html", locals())

def edit_risques(request, pk):
    get_famillerisk = requests.get(f"{listerisque}{pk}")
    data = get_famillerisk.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    filiale = request.session.get('filiale')
    data_filiale_list = [data for data in data_filiale_list if data["sigle_filiale"] == filiale]
    if request.method == "POST":
        coderisk = request.POST.get('coderisk')
        idfiliale = request.POST.get('idfiliale')
        # Données à envoyer dans la requête POST
        data = {
                "coderisk": coderisk,
                "idfiliale": int(idfiliale),
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{listerisque}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/risques/form_risques.html", locals())

def add_risques(request):
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    filiale = request.session.get('filiale')
    data_filiale_list = [data for data in data_filiale_list if data["sigle_filiale"] == filiale]
    if request.method == "POST":
        coderisk = request.POST.get('coderisk')
        idfiliale = request.POST.get('idfiliale')
        # Données à envoyer dans la requête POST
        data = {
                "coderisk": coderisk,
                "idfiliale": int(idfiliale),
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listerisque}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/risques/form_risques.html", locals())

def del_risques(request, pk):
    get_famillerisk = requests.get(f"{listerisque}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listerisque}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/risques/del_risques.html", locals())
