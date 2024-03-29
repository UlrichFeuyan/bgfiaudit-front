import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def mise_a_jour_tpa(request):
    dropdown_mission = 'True'
    mise_a_jour_tpa_active = 'True'
    return render(request, 'services/mise_a_jour_tpa/mise_a_jour_tpa.html', locals())

def list_mise_a_jour_tpa(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/mise_a_jour_tpa/list_mise_a_jour_tpa.html", locals())

def edit_mise_a_jour_tpa(request, pk):
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
    return render(request, "services/mise_a_jour_tpa/form_mise_a_jour_tpa.html", locals())

def add_mise_a_jour_tpa(request):
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
    return render(request, "services/mise_a_jour_tpa/form_mise_a_jour_tpa.html", locals())

def del_mise_a_jour_tpa(request, pk):
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
    return render(request, "services/mise_a_jour_tpa/del_mise_a_jour_tpa.html", locals())
