import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def profil_utilisateur(request):
    profile_utilisateur_active = 'True'
    dropdown_profils = 'True'
    return render(request, 'services/profil_utilisateur/profil_utilisateur.html', locals())

def list_profil_utilisateur(request):
    get_data = requests.get(listeprofil)
    data_list = get_data.json()
    return render(request, "services/profil_utilisateur/list_profil_utilisateur.html", locals())

def edit_profil_utilisateur(request, pk):
    get_famillerisk = requests.get(f"{listeprofil}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('lib_profil_user')
         # Données à envoyer dans la requête POST
        data = {
                "lib_profil_user": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listeprofil}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/profil_utilisateur/form_profil_utilisateur.html", locals())

def add_profil_utilisateur(request):
    if request.method == "POST":
        value = request.POST.get('lib_profil_user')
         # Données à envoyer dans la requête POST
        data = {
                "lib_profil_user": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listeprofil}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/profil_utilisateur/form_profil_utilisateur.html", locals())

def del_profil_utilisateur(request, pk):
    get_famillerisk = requests.get(f"{listeprofil}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listeprofil}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/profil_utilisateur/del_profil_utilisateur.html", locals())
