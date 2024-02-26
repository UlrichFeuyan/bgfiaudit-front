import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def gravite_de_risques(request):
    dropdown_parametre_generaux = 'True'
    gravite_risque_active = 'True'
    return render(request, 'services/gravite_de_risques/gravite_de_risques.html', locals())

def list_gravite_de_risques(request):
    get_data = requests.get(listegraviterisk)
    data_list = get_data.json()
    return render(request, "services/gravite_de_risques/list_gravite_de_risques.html", locals())

def edit_gravite_de_risques(request, pk):
    get_famillerisk = requests.get(f"{listegraviterisk}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libgraviterisk": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listegraviterisk}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/gravite_de_risques/form_gravite_de_risques.html", locals())

def add_gravite_de_risques(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libgraviterisk": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listegraviterisk}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/gravite_de_risques/form_gravite_de_risques.html", locals())

def del_gravite_de_risques(request, pk):
    get_famillerisk = requests.get(f"{listegraviterisk}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listegraviterisk}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/gravite_de_risques/del_gravite_de_risques.html", locals())
