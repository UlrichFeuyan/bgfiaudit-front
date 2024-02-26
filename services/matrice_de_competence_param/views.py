import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def matrice_de_competence_param(request):
    dropdown_parametre_filiale = 'True'
    matrice_competence_param_active = 'True'
    return render(request, 'services/matrice_de_competence_param/matrice_de_competence_param.html', locals())

def list_matrice_de_competence_param(request):
    get_data = requests.get(listeCompetences)
    data_list = get_data.json()
    return render(request, "services/matrice_de_competence_param/list_matrice_de_competence_param.html", locals())

def edit_matrice_de_competence_param(request, pk):
    get_famillerisk = requests.get(f"{listeCompetences}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        lib_competences = request.POST.get('lib_competences')
         # Données à envoyer dans la requête POST
        data = {
                "lib_competences": lib_competences,
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listeCompetences}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/matrice_de_competence_param/form_matrice_de_competence_param.html", locals())

def add_matrice_de_competence_param(request):
    if request.method == "POST":
        lib_competences = request.POST.get('lib_competences')
         # Données à envoyer dans la requête POST
        data = {
                "lib_competences": lib_competences,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listeCompetences}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/matrice_de_competence_param/form_matrice_de_competence_param.html", locals())

def del_matrice_de_competence_param(request, pk):
    get_famillerisk = requests.get(f"{listeCompetences}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listeCompetences}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/matrice_de_competence_param/del_matrice_de_competence_param.html", locals())
