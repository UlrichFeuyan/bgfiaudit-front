import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def systeme(request):
    dropdown_parametre_filiale = 'True'
    systeme_active = 'True'
    return render(request, 'services/systeme/systeme.html', locals())

def list_systeme(request):
    get_data = requests.get(listesysteme)
    data_list = get_data.json()

    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    return render(request, "services/systeme/list_systeme.html", locals())

def edit_systeme(request, pk):
    get_famillerisk = requests.get(f"{listesysteme}{pk}")
    data = get_famillerisk.json()

    get_processus = requests.get(listeProcessus)
    processus = get_processus.json()

    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    if request.method == "POST":
        libsys = request.POST.get('libsys')
        idfiliale = request.POST.get('idfiliale')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "libsys": libsys,
                    "idfiliale": int(idfiliale),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.patch(f"{listesysteme}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/systeme/form_systeme.html", locals())

def add_systeme(request):
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    if request.method == "POST":
        libsys = request.POST.get('libsys')
        idfiliale = request.POST.get('idfiliale')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "libsys": libsys,
                    "idfiliale": int(idfiliale),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.post(f"{listesysteme}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/systeme/form_systeme.html", locals())

def del_systeme(request, pk):
    get_famillerisk = requests.get(f"{listesysteme}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listesysteme}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/systeme/del_systeme.html", locals())


def detail_processus_systeme(request, pk):
    get_systeme = requests.get(f"{listesysteme}{pk}")
    data_systeme = get_systeme.json()
    get_systeme_processus = requests.get(f"{listesys_processus}")
    data_systeme_processus = get_systeme_processus.json()
    processus = []

    for process_systeme in data_systeme_processus:
        if data_systeme["id_sys"] == process_systeme["id_sys"]:
            id_processus = process_systeme["id_processus"]
            get_processus = requests.get(f"{listeProcessus}{id_processus}")
            data_processus = get_processus.json()
            processus.append(data_processus)
    return render(request, "services/systeme/detail_processus_systeme.html", locals())
