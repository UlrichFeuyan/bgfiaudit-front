import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def site(request):
    dropdown_parametre_filiale = 'True'
    site_active = 'True'
    header_title= "Site"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'paramétrages filiale',
            },
            {
                'name': 'site',
            },
        ]
    return render(request, 'services/site/site.html', locals())

def list_site(request):
    get_data = requests.get(listesite)
    data_list = get_data.json()

    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    return render(request, "services/site/list_site.html", locals())

def edit_site(request, pk):
    get_famillerisk = requests.get(f"{listesite}{pk}")
    data = get_famillerisk.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    if request.method == "POST":
        lib_site = request.POST.get('lib_site')
        idfiliale = request.POST.get('idfiliale')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "lib_site": lib_site,
                    "idfiliale": int(idfiliale),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.patch(f"{listesite}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"Site N°Modifié."
                })
            }
        )
    return render(request, "services/site/form_site.html", locals())

def add_site(request):
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    if request.method == "POST":
        lib_site = request.POST.get('lib_site')
        idfiliale = request.POST.get('idfiliale')
        # Données à envoyer dans la requête POST
        try:
            data = {
                    "lib_site": lib_site,
                    "idfiliale": int(idfiliale),
                    }
        except Exception as e:
            return JsonResponse({"error": f"{str(e)}"})
        # Faire une requête POST à l'API
        response = requests.post(f"{listesite}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/site/form_site.html", locals())

def del_site(request, pk):
    get_famillerisk = requests.get(f"{listesite}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listesite}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/site/del_site.html", locals())
