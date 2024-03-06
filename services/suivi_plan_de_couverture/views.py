import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def suivi_plan_de_couverture(request):
    dropdown_mission = 'True'
    suivi_plan_couverture_active = 'True'
    return render(request, 'services/suivi_plan_de_couverture/controles.html', locals())

def list_suivi_plan_de_couverture(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/suivi_plan_de_couverture/list_suivi_plan_de_couverture.html", locals())

def edit_suivi_plan_de_couverture(request, pk):
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
    return render(request, "services/suivi_plan_de_couverture/form_suivi_plan_de_couverture.html", locals())

def add_suivi_plan_de_couverture(request):
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
    return render(request, "services/suivi_plan_de_couverture/form_suivi_plan_de_couverture.html", locals())

def del_suivi_plan_de_couverture(request, pk):
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
    return render(request, "services/suivi_plan_de_couverture/del_suivi_plan_de_couverture.html", locals())
