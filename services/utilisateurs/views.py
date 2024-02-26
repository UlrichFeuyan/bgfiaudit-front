import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def utilisateurs(request):
    utilisateurs_active = 'True'
    return render(request, 'services/utilisateurs/utilisateurs.html', locals())

def list_utilisateurs(request):
    get_filiale_liste = requests.get(listeFiliale)
    filiale_liste = get_filiale_liste.json()
    get_data = requests.get(ges_user)
    data_list = get_data.json()
    return render(request, "services/utilisateurs/list_utilisateurs.html", locals())

def edit_utilisateurs(request, pk):
    get_filiale = requests.get(listeFiliale)
    get_profil = requests.get(listeprofil)
    filialeList = get_filiale.json()
    profilList = get_profil.json()
    get_user = requests.get(f"{ges_user}{pk}")
    data = get_user.json()
    if request.method == "POST":
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        idprofil_user = request.POST.get('idprofil_user')
        idfiliale = request.POST.get('idfiliale')

        # Faire des requêtes pour récupérer le profil et la filiale
        profil_response = requests.get(f"{listeprofil}{idprofil_user}")
        filiale_response = requests.get(f"{gestfiliale}{idfiliale}")

        # Extraire les données pertinentes des réponses
        profil_data = profil_response.json()
        filiale_data = filiale_response.json()

        # Données à envoyer dans la requête POST
        data = {
                "username": username,
                "last_name": last_name,
                "first_name": first_name,
                "email": email,
                "idprofil_user": int(idprofil_user),
                "idfiliale": int(idfiliale),
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{ges_user}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/utilisateurs/form_utilisateurs.html", locals())

def add_utilisateurs(request):
    get_filiale = requests.get(listeFiliale)
    get_profil = requests.get(listeprofil)
    filialeList = get_filiale.json()
    profilList = get_profil.json()
    if request.method == "POST":
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        idprofil_user = request.POST.get('idprofil_user')
        idfiliale = request.POST.get('idfiliale')

        # Faire des requêtes pour récupérer le profil et la filiale
        profil_response = requests.get(f"{listeprofil}{idprofil_user}")
        filiale_response = requests.get(f"{gestfiliale}{idfiliale}")

        # Extraire les données pertinentes des réponses
        profil_data = profil_response.json()
        filiale_data = filiale_response.json()

        # Données à envoyer dans la requête POST
        data = {
                "username": username,
                "last_name": last_name,
                "first_name": first_name,
                "email": email,
                "idprofil_user": int(idprofil_user),
                "idfiliale": int(idfiliale),
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{ges_user}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/utilisateurs/form_utilisateurs.html", locals())

def reset_password(request, pk):
    get_famillerisk = requests.get(f"{ges_user}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.post(f"{ges_user}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/utilisateurs/reset_password_utilisateurs.html", locals())

def del_utilisateurs(request, pk):
    get_famillerisk = requests.get(f"{ges_user}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{ges_user}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/utilisateurs/del_utilisateurs.html", locals())
