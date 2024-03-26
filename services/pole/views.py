import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def pole(request):
    dropdown_parametre_filiale = 'True'
    pole_active = 'True'
    header_title= "Pole"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'paramétrages filiale',
            },
            {
                'name': 'pole',
            },
        ]
    return render(request, 'services/pole/pole.html', locals())

def list_pole(request):
    get_data = requests.get(listePole)
    data_list = get_data.json()

    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    return render(request, "services/pole/list_pole.html", locals())

def edit_pole(request, pk):
    get_famillerisk = requests.get(f"{listePole}{pk}")
    data = get_famillerisk.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    filiale = request.session.get('filiale')
    data_filiale_list = [data for data in data_filiale_list if data["sigle_filiale"] == filiale]
    if request.method == "POST":
        libpole = request.POST.get('libpole')
        managerpole = request.POST.get('managerpole')
        idfiliale = request.POST.get('idfiliale')
        # Données à envoyer dans la requête POST
        data = {
                "libpole": libpole,
                "managerpole": managerpole,
                "idfiliale": idfiliale,
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listePole}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/pole/form_pole.html", locals())

def add_pole(request):
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    filiale_courante = request.session.get('filiale')
    data_filiale_list = [data for data in data_filiale_list if data["sigle_filiale"] == filiale_courante]
    if request.method == "POST":
        libpole = request.POST.get('libpole')
        managerpole = request.POST.get('managerpole')
        idfiliale = request.POST.get('idfiliale')
         # Données à envoyer dans la requête POST
        data = {
                "libpole": libpole,
                "managerpole": managerpole,
                "idfiliale": idfiliale,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listePole}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/pole/form_pole.html", locals())

def del_pole(request, pk):
    get_famillerisk = requests.get(f"{listePole}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listePole}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/pole/del_pole.html", locals())
