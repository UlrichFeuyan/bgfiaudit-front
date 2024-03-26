import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def evaluations_impact_risque(request):
    dropdown_parametre_generaux = 'True'
    evaluation_impact_risque_active = 'True'
    header_title= "Evaluation impact de risque"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
             {
                'name': 'paramétrages',
            },
            {
                'name': 'évaluation impact de risque',
            },
        ]
    return render(request, 'services/evaluations_impact_risque/evaluations_impact_risque.html', locals())

def list_evaluations_impact_risque(request):
    get_data = requests.get(evalimpactrisk)
    data_list = get_data.json()
    return render(request, "services/evaluations_impact_risque/list_evaluations_impact_risque.html", locals())

def edit_evaluations_impact_risque(request, pk):
    get_famillerisk = requests.get(f"{listefamillerisk}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libfamillerisk": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listefamillerisk}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/evaluations_impact_risque/form_evaluations_impact_risque.html", locals())

def add_evaluations_impact_risque(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libfamillerisk": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listefamillerisk}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/evaluations_impact_risque/form_evaluations_impact_risque.html", locals())

def del_evaluations_impact_risque(request, pk):
    get_famillerisk = requests.get(f"{listefamillerisk}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listefamillerisk}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/evaluations_impact_risque/del_evaluations_impact_risque.html", locals())
