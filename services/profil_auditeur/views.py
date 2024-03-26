import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def profil_auditeur(request):
    profile_auditeur_active = 'True'
    dropdown_profils = 'True'
    header_title= "Profil auditeur"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'profils',
            },
            {
                'name': 'profil auditeur',
            },
        ]
    return render(request, 'services/profil_auditeur/profil_auditeur.html', locals())

def list_profil_auditeur(request):
    get_data = requests.get(listeprofilauditeur)
    data_list = get_data.json()
    return render(request, "services/profil_auditeur/list_profil_auditeur.html", locals())

def edit_profil_auditeur(request, pk):
    get_famillerisk = requests.get(f"{listeprofilauditeur}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "lib_profil_audit": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listeprofilauditeur}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/profil_auditeur/form_profil_auditeur.html", locals())

def add_profil_auditeur(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "lib_profil_audit": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listeprofilauditeur}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/profil_auditeur/form_profil_auditeur.html", locals())

def del_profil_auditeur(request, pk):
    get_famillerisk = requests.get(f"{listeprofilauditeur}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listeprofilauditeur}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/profil_auditeur/del_profil_auditeur.html", locals())
