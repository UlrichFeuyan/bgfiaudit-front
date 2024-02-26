import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def risques(request):
    dropdown_activite_risque = 'True'
    risque_active = 'True'
    return render(request, 'services/risques/risques.html', locals())

def list_risques(request):
    get_data = requests.get(listerisque)
    data_list = get_data.json()
    return render(request, "services/risques/list_risques.html", locals())

def edit_risques(request, pk):
    get_famillerisk = requests.get(f"{listerisque}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        coderisk = request.POST.get('coderisk')
        sigle_filiale = request.POST.get('sigle_filiale')
         # Données à envoyer dans la requête POST
        data = {
                "coderisk": coderisk,
                "sigle_filiale": sigle_filiale,
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
    if request.method == "POST":
        coderisk = request.POST.get('coderisk')
        sigle_filiale = request.POST.get('sigle_filiale')
        # Données à envoyer dans la requête POST
        data = {
                "coderisk": coderisk,
                "sigle_filiale": sigle_filiale,
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
