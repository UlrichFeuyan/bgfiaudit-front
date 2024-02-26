import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def matrice_de_competence(request):
    dropdown_auditeur = 'True'
    matrice_competence_active = 'True'
    return render(request, 'services/matrice_de_competence/matrice_de_competence.html', locals())

def list_matrice_de_competence(request):
    get_utilisateurs = requests.get(listeUtilisateur)
    utilisateurs = get_utilisateurs.json()
    get_data = requests.get(listeCompetences)
    data_list = get_data.json()
    return render(request, "services/matrice_de_competence/list_matrice_de_competence.html", locals())

def edit_matrice_de_competence(request, pk):
    get_famillerisk = requests.get(f"{listeCompetences}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libfamillerisk": f"{value}"
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
    return render(request, "services/matrice_de_competence/form_matrice_de_competence.html", locals())

def add_matrice_de_competence(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libfamillerisk": f"{value}"
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
    return render(request, "services/matrice_de_competence/form_matrice_de_competence.html", locals())

def del_matrice_de_competence(request, pk):
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
    return render(request, "services/matrice_de_competence/del_matrice_de_competence.html", locals())
