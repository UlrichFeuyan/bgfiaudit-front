import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def gestions_des_filiales(request):
    gestion_filiale_active = 'True'
    header_title= "Gestion des filiales"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'gestion des filiales',
            },
        ]
    return render(request, 'services/gestions_des_filiales/gestions_des_filiales.html', locals())

def list_gestions_des_filiales(request):
    get_data = requests.get(gestfiliale)
    data_list = get_data.json()
    return render(request, "services/gestions_des_filiales/list_gestions_des_filiales.html", locals())

def edit_gestions_des_filiales(request, pk):
    get_famillerisk = requests.get(f"{gestfiliale}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        sigle_filiale = request.POST.get('sigle_filiale')
        nom_filiale = request.POST.get('nom_filiale')
        code_pays = request.POST.get('code_pays')
        dg_filiale = request.POST.get('dg_filiale')
        adresse_filiale = request.POST.get('adresse_filiale')
        ville_filiale = request.POST.get('ville_filiale')
        description_filiale = request.POST.get('description_filiale')
        tel_filiale = request.POST.get('tel_filiale')
        mob_filiale = request.POST.get('mob_filiale')
        fax_filiale = request.POST.get('fax_filiale')
        email_filiale = request.POST.get('email_filiale')
        adresseip_smtp = request.POST.get('adresseip_smtp')
        port_smtp = request.POST.get('port_smtp')
        j_relances = request.POST.get('j_relances')
        j_statistiques = request.POST.get('j_statistiques')
        smtp_user = request.POST.get('smtp_user')
        smtp_password = request.POST.get('smtp_password')
         # Données à envoyer dans la requête POST
        data = {
                "sigle_filiale": sigle_filiale,
                "nom_filiale": nom_filiale,
                "code_pays": code_pays,
                "dg_filiale": dg_filiale,
                "adresse_filiale": adresse_filiale,
                "ville_filiale": ville_filiale,
                "description_filiale": description_filiale,
                "tel_filiale": tel_filiale,
                "mob_filiale": mob_filiale,
                "fax_filiale": fax_filiale,
                "email_filiale": email_filiale,
                "adresseip_smtp": adresseip_smtp,
                "port_smtp": port_smtp,
                "j_relances": j_relances,
                "j_statistiques": j_statistiques,
                "smtp_user": smtp_user,
                "smtp_password": smtp_password,
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{gestfiliale}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/gestions_des_filiales/form_gestions_des_filiales.html", locals())

def add_gestions_des_filiales(request):
    if request.method == "POST":
        sigle_filiale = request.POST.get('sigle_filiale')
        nom_filiale = request.POST.get('nom_filiale')
        code_pays = request.POST.get('code_pays')
        dg_filiale = request.POST.get('dg_filiale')
        adresse_filiale = request.POST.get('adresse_filiale')
        ville_filiale = request.POST.get('ville_filiale')
        description_filiale = request.POST.get('description_filiale')
        tel_filiale = request.POST.get('tel_filiale')
        mob_filiale = request.POST.get('mob_filiale')
        fax_filiale = request.POST.get('fax_filiale')
        email_filiale = request.POST.get('email_filiale')
        adresseip_smtp = request.POST.get('adresseip_smtp')
        port_smtp = request.POST.get('port_smtp')
        j_relances = request.POST.get('j_relances')
        j_statistiques = request.POST.get('j_statistiques')
        smtp_user = request.POST.get('smtp_user')
        smtp_password = request.POST.get('smtp_password')
         # Données à envoyer dans la requête POST
        data = {
                "sigle_filiale": sigle_filiale,
                "nom_filiale": nom_filiale,
                "code_pays": code_pays,
                "dg_filiale": dg_filiale,
                "adresse_filiale": adresse_filiale,
                "ville_filiale": ville_filiale,
                "description_filiale": description_filiale,
                "tel_filiale": tel_filiale,
                "mob_filiale": mob_filiale,
                "fax_filiale": fax_filiale,
                "email_filiale": email_filiale,
                "adresseip_smtp": adresseip_smtp,
                "port_smtp": port_smtp,
                "j_relances": j_relances,
                "j_statistiques": j_statistiques,
                "smtp_user": smtp_user,
                "smtp_password": smtp_password,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{gestfiliale}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/gestions_des_filiales/form_gestions_des_filiales.html", locals())

def del_gestions_des_filiales(request, pk):
    get_famillerisk = requests.get(f"{gestfiliale}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{gestfiliale}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/gestions_des_filiales/del_gestions_des_filiales.html", locals())
