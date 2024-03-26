import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def sys_processus(request):
    dropdown_parametre_filiale = 'True'
    sys_processus_active = 'True'
    return render(request, 'services/sys_processus/sys_processus.html', locals())

def list_sys_processus(request):
    get_data = requests.get(listesys_processus)
    data_list = get_data.json()

    get_data_pole = requests.get(listePole)
    data_list_pole = get_data_pole.json()
    return render(request, "services/sys_processus/list_sys_processus.html", locals())

def edit_sys_processus(request, pk):
    get_famillerisk = requests.get(f"{listesys_processus}{pk}")
    data = get_famillerisk.json()
    get_data_pole = requests.get(listePole)
    data_list_pole = get_data_pole.json()
    if request.method == "POST":
        libsys_processus = request.POST.get('libsys_processus')
        pilotesys_processus = request.POST.get('pilotesys_processus')
        idpole = request.POST.get('idpole')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "libsys_processus": libsys_processus,
                    "pilotesys_processus": pilotesys_processus,
                    "idpole": int(idpole),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.patch(f"{listesys_processus}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/sys_processus/form_sys_processus.html", locals())

def add_sys_processus(request):
    get_data_pole = requests.get(listePole)
    data_list_pole = get_data_pole.json()
    if request.method == "POST":
        libsys_processus = request.POST.get('libsys_processus')
        pilotesys_processus = request.POST.get('pilotesys_processus')
        idpole = request.POST.get('idpole')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "libsys_processus": libsys_processus,
                    "pilotesys_processus": pilotesys_processus,
                    "idpole": int(idpole),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.post(f"{listesys_processus}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/sys_processus/form_sys_processus.html", locals())

def del_sys_processus(request, pk):
    get_famillerisk = requests.get(f"{listesys_processus}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listesys_processus}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/sys_processus/del_sys_processus.html", locals())
