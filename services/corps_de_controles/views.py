import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def corps_de_controles(request):
    dropdown_parametre_generaux = 'True'
    corps_control_active = 'True'
    header_title= "Corps de contrôle"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'paramétrages',
            },
            {
                'name': 'corps de controle',
            },
        ]
    return render(request, 'services/corps_de_controles/corps_de_controles.html', locals())

def list_corps_de_controles(request):
    get_data = requests.get(corpsdecontrole)
    data_list = get_data.json()
    return render(request, "services/corps_de_controles/list_corps_de_controles.html", locals())

def edit_corps_de_controles(request, pk):
    get_famillerisk = requests.get(f"{listecontrole}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libcorpsdecontrole": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listecontrole}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/corps_de_controles/form_corps_de_controles.html", locals())

def add_corps_de_controles(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libcorpsdecontrole": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listecontrole}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/corps_de_controles/form_corps_de_controles.html", locals())

def del_corps_de_controles(request, pk):
    get_famillerisk = requests.get(f"{listecontrole}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listecontrole}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/corps_de_controles/del_corps_de_controles.html", locals())
