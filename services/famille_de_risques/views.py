import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.urls import reverse_lazy, reverse


def famille_de_risques(request):
    dropdown_parametre_generaux = 'True'
    famille_risque_active = 'True'
    header_title= "Famille de risque"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'paramétrages',
            },
            {
                'name': 'famille de risque',
            },
        ]
    return render(request, 'services/famille_de_risques/famille_de_risques.html', locals())

def list_famille_de_risques(request):
    get_data = requests.get(listefamillerisk)
    data_list = get_data.json()
    return render(request, "services/famille_de_risques/list_famille_de_risques.html", locals())

def edit_famille_de_risques(request, pk):
    modal_title = "Famille de risque"
    action = reverse("services:edit_famille_de_risques",  kwargs={'pk': pk})
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
    return render(request, "services/famille_de_risques/form_famille_de_risques.html", locals())

def add_famille_de_risques(request):
    modal_title = "Famille de risque"
    action = reverse("services:add_famille_de_risques")
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
    return render(request, "services/famille_de_risques/form_famille_de_risques.html", locals())

def del_famille_de_risques(request, pk):
    get_famillerisk = requests.get(f"{listefamillerisk}{pk}")
    data = get_famillerisk.json()
    modal_title = "Famille de risque"
    action = reverse("services:del_famille_de_risques",  kwargs={'pk': pk})
    if request.method == "POST":
        response = requests.delete(f"{listefamillerisk}{pk}")
        # sweetify.info(request, "Enregistrement supprimé", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/famille_de_risques/del_famille_de_risques.html", locals())
