import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def gestions_des_filiales(request):
    gestion_filiale_active = 'True'
    return render(request, 'services/gestions_des_filiales/gestions_des_filiales.html', locals())

def list_gestions_des_filiales(request):
    get_data = requests.get(gestfiliale)
    data_list = get_data.json()
    return render(request, "services/gestions_des_filiales/list_gestions_des_filiales.html", locals())

def edit_gestions_des_filiales(request, pk):
    get_famillerisk = requests.get(f"{gestfiliale}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        sigle_filiale = request.POST.get('sigle_filiale')
        nom_filiale = request.POST.get('nom_filiale')
        pays_filiale = request.POST.get('pays_filiale')
        dg_filiale = request.POST.get('dg_filiale')
        adresse_filiale = request.POST.get('adresse_filiale')
         # Données à envoyer dans la requête POST
        data = {
                "sigle_filiale": sigle_filiale,
                "nom_filiale": nom_filiale,
                "pays_filiale": pays_filiale,
                "dg_filiale": dg_filiale,
                "adresse_filiale": adresse_filiale,
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{gestfiliale}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/gestions_des_filiales/form_gestions_des_filiales.html", locals())

def add_gestions_des_filiales(request):
    if request.method == "POST":
        sigle_filiale = request.POST.get('sigle_filiale')
        nom_filiale = request.POST.get('nom_filiale')
        pays_filiale = request.POST.get('pays_filiale')
        dg_filiale = request.POST.get('dg_filiale')
        adresse_filiale = request.POST.get('adresse_filiale')
         # Données à envoyer dans la requête POST
        data = {
                "sigle_filiale": sigle_filiale,
                "nom_filiale": nom_filiale,
                "pays_filiale": pays_filiale,
                "dg_filiale": dg_filiale,
                "adresse_filiale": adresse_filiale,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{gestfiliale}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/gestions_des_filiales/form_gestions_des_filiales.html", locals())

def del_gestions_des_filiales(request, pk):
    get_famillerisk = requests.get(f"{gestfiliale}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{gestfiliale}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/gestions_des_filiales/del_gestions_des_filiales.html", locals())
