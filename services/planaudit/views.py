import json
import requests

from services.tables import PlanAuditTable
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from ..models import Document
import pandas
import sweetify
import unicodedata
from datetime import datetime
dt = datetime.now()
annee_actuelle = dt.strftime('%Y')

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def planaudit(request):
    dropdown_mission = "True"
    plan_audit_active = "True"
    return render(request, 'services/planaudit/planaudit.html', locals())

def list_planaudit(request):
    get_data = requests.get(listeplanaudit)
    data_list = get_data.json()

    get_data_systeme = requests.get(listesysteme)
    get_data_processus = requests.get(listeProcessus)
    get_data_site = requests.get(listesite)
    data_systeme_list = get_data_systeme.json()
    data_processus_list = get_data_processus.json()
    data_site_list = get_data_site.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    return render(request, "services/planaudit/list_planaudit.html", locals())

def list_planannuel(request):
    get_data = requests.get(listeplanaudit)
    data_list = get_data.json()

    data_list = [data for data in data_list if data["annee_theo_proch"] == annee_actuelle and data["valid_plan"]]
    get_data_systeme = requests.get(listesysteme)
    get_data_processus = requests.get(listeProcessus)
    get_data_site = requests.get(listesite)
    data_systeme_list = get_data_systeme.json()
    data_processus_list = get_data_processus.json()
    data_site_list = get_data_site.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    return render(request, "services/planaudit/list_planaudit.html", locals())


def edit_planaudit(request, pk):
    get_famillerisk = requests.get(f"{listeplanaudit}{pk}")
    data = get_famillerisk.json()

    get_data_systeme = requests.get(listesysteme)
    get_data_processus = requests.get(listeProcessus)
    get_data_site = requests.get(listesite)
    data_systeme_list = get_data_systeme.json()
    data_processus_list = get_data_processus.json()
    data_site_list = get_data_site.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()
    edition = "True"
    if request.method == "POST":
        idfiliale = request.POST.get('idfiliale')
        anne_ref_cycle = request.POST.get('anne_ref_cycle')
        idsysteme = request.POST.get('idsysteme')
        idprocessus = request.POST.get('idprocessus')
        idsite = request.POST.get('idsite')
        criticite_carto = request.POST.get('criticite_carto')
        annee_theo_last_audit = request.POST.get('annee_theo_last_audit')
        annee_eff_last_audit = request.POST.get('annee_eff_last_audit')
        criticite_audit = request.POST.get('criticite_audit')
        annee_theo_proch = request.POST.get('annee_theo_proch')
        # Données à envoyer dans la requête POST
        data = {
                "idfiliale": int(idfiliale),
                "anne_ref_cycle": anne_ref_cycle,
                "idsysteme": int(idsysteme),
                "idprocessus": int(idprocessus),
                "idsite": int(idsite),
                "criticite_carto": criticite_carto,
                "annee_theo_last_audit": annee_theo_last_audit,
                "annee_eff_last_audit": annee_eff_last_audit,
                "criticite_audit": criticite_audit,
                "annee_theo_proch": annee_theo_proch,
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{listeplanaudit}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/planaudit/form_planaudit.html", locals())

def add_planaudit(request):
    get_data_systeme = requests.get(listesysteme)
    get_data_processus = requests.get(listeProcessus)
    get_data_site = requests.get(listesite)
    data_systeme_list = get_data_systeme.json()
    data_processus_list = get_data_processus.json()
    data_site_list = get_data_site.json()
    get_data_filiale = requests.get(gestfiliale)
    data_filiale_list = get_data_filiale.json()

    if request.method == "POST":
        idfiliale = request.POST.get('idfiliale')
        anne_ref_cycle = request.POST.get('anne_ref_cycle')
        idsysteme = request.POST.get('idsysteme')
        idprocessus = request.POST.get('idprocessus')
        idsite = request.POST.get('idsite')
        criticite_carto = request.POST.get('criticite_carto')
        annee_theo_last_audit = request.POST.get('annee_theo_last_audit')
        annee_eff_last_audit = request.POST.get('annee_eff_last_audit')
        criticite_audit = request.POST.get('criticite_audit')
        annee_theo_proch = request.POST.get('annee_theo_proch')
        # Données à envoyer dans la requête POST
        data = {
                "idfiliale": int(idfiliale),
                "anne_ref_cycle": anne_ref_cycle,
                "idsysteme": int(idsysteme),
                "idprocessus": int(idprocessus),
                "idsite": int(idsite),
                "criticite_carto": criticite_carto,
                "annee_theo_last_audit": annee_theo_last_audit,
                "annee_eff_last_audit": annee_eff_last_audit,
                "criticite_audit": criticite_audit,
                "annee_theo_proch": annee_theo_proch,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listeplanaudit}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/planaudit/form_planaudit.html", locals())

def del_planaudit(request, pk):
    get_famillerisk = requests.get(f"{listeplanaudit}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listeplanaudit}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/planaudit/del_planaudit.html", locals())

def import_excel_plan_audit(request):
    return render(request, "services/planaudit/import_excel.html", locals())

def document_list(request):
    if request.method == "POST" and request.FILES.get("fichier_excel"):
        fichier_excel = request.FILES["fichier_excel"]
        df = pandas.read_excel('fichier.xlsx')
        documents = [
            Document(
                fillale=row[0],
                annee_de_reference=row[1],
                systeme=row[2],
                processus=row[3],
                site=row[4],
                criticité_issue_de_la_cartographie_des_risques=row[5],
                annee_théorique_du_dernier_audit=row[6],
                annee_de_réalisation=row[7],
                criticité_issue_de_la_mission_d_audit=row[8],
                annee_de_la_prochaine_mission_d_audit=row[9],
            )
            for row in df.values
        ]
    context = {
        'documents': documents,
    }
    return render(request, 'document_list.html', context)

def convert_to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def import_plan_audit(request):
    if request.method == "POST" and request.FILES.get("fichier_excel"):
        fichier_excel = request.FILES['fichier_excel']
        # Importer le fichier Excel et convertir en une liste d'objets Document

        df = pandas.read_excel(fichier_excel)
        # Remplacer les valeurs NaN par une chaîne vide ou une autre valeur par défaut
        df.fillna('', inplace=True)
        # Convertir toutes les valeurs en chaînes de caractères
        # df = df.astype(str)
        try:
            documents = [
                Document(
                    fillale=row[0],
                    annee_de_reference=row[1],
                    systeme=row[2],
                    processus=row[3],
                    site=row[4],
                    criticite_issue_de_la_cartographie_des_risques=row[5],
                    annee_theorique_du_dernier_audit=convert_to_int(row[6]),
                    annee_de_realisation=convert_to_int(row[7]),
                    criticite_issue_de_la_mission_d_audit=row[8],
                    annee_de_la_prochaine_mission_d_audit=convert_to_int(row[9]),
                )
                for row in df.values
            ]
            Document.objects.bulk_create(documents)
            messages.success(request, "Les données ont été importées avec succès.")
        except Exception as e:
            print(f"Erreur : {str(e)}")

        return redirect("services:validation_plan_audit")
    return render(request, "services/planaudit/import_planaudit.html", locals())

def validation_plan_audit(request):
    return render(request, "services/planaudit/validation_excel.html", locals())


class validationPlanAuditListView(ListView):
    model = Document
    template_name = 'services/planaudit/validation_excel.html'
    context_object_name = 'documents'

criticies = {
    'FAIBLE': 1,
    'MODERE': 2,
    'ELEVE': 3,
    'CRITIQUE': 4,
}

def upload_plan_audit(request):
    document_list = Document.objects.all()

    filiales = requests.get(gestfiliale)
    filiales = filiales.json()

    systemes = requests.get(listesysteme)
    systemes = systemes.json()

    process = requests.get(listeProcessus)
    process = process.json()

    sites = requests.get(listesite)
    sites = sites.json()
    """try:"""
    data_list = []
    for document in document_list:
        filiale = document.fillale
        annee_de_reference = document.annee_de_reference
        systeme = document.systeme
        processus = document.processus
        site = document.site
        criticite_issue_de_la_cartographie_des_risques = document.criticite_issue_de_la_cartographie_des_risques
        annee_theorique_du_dernier_audit = document.annee_theorique_du_dernier_audit
        annee_de_realisation = document.annee_de_realisation
        criticite_issue_de_la_mission_d_audit = document.criticite_issue_de_la_mission_d_audit
        annee_de_la_prochaine_mission_d_audit = document.annee_de_la_prochaine_mission_d_audit

        idfiliale_list = [f["idfiliale"] for f in filiales if remove_accents(f["sigle_filiale"].upper())==remove_accents(filiale.upper())]
        idfiliale = idfiliale_list[0] if idfiliale_list else None

        idsysteme_list = [s["id_sys"] for s in systemes if remove_accents(s["libsys"].upper())==remove_accents(systeme.upper())]
        idsysteme = idsysteme_list[0] if idsysteme_list else None

        idprocessus_list = [p["idprocessus"] for p in process if remove_accents(p["libprocessus"].upper())==remove_accents(processus.upper())]
        idprocessus = idprocessus_list[0] if idprocessus_list else None

        idsite_list = [s["id_site"] for s in sites if remove_accents(s["lib_site"].upper())==remove_accents(site.upper())]
        idsite = idsite_list[0] if idsite_list else None


        data = {
                "idfiliale": idfiliale,
                "anne_ref_cycle": annee_de_reference,
                "idsysteme": idsysteme,
                "idprocessus": idprocessus,
                "idsite": idsite,
                "criticite_carto": criticies[f"{remove_accents(criticite_issue_de_la_cartographie_des_risques.upper())}"],
                "annee_theo_last_audit": annee_theorique_du_dernier_audit,
                "annee_eff_last_audit": annee_de_realisation,
                "criticite_audit": criticies[f"{remove_accents(criticite_issue_de_la_mission_d_audit.upper())}"],
                "annee_theo_proch": annee_de_la_prochaine_mission_d_audit,
            }
        data_list.append(data)
    """except Exception as e:
        print(f"erreur : {str(e)}")
        sweetify.error(request, f"Une est survenue lors de la validation des données", showConfirmButton=False, timer=4000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
        return redirect('services:planaudit')"""
    for data in data_list:
        response = requests.post(f"{listeplanaudit}", data=data)
    sweetify.info(request, "Enregistrements Ajoutés!", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
    Document.objects.all().delete()
    return redirect('services:planaudit')

@csrf_exempt
def save_document_plan_adit(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    document=Document.objects.get(id=id)
    if type == "fillale":
       document.fillale=value

    if type == "annee_de_reference":
        document.annee_de_reference = value

    if type == "systeme":
        document.systeme = value

    if type == "processus":
        document.processus = value

    if type == "site":
        document.site = value

    if type == "criticite_issue_de_la_cartographie_des_risques":
        document.criticite_issue_de_la_cartographie_des_risques = value

    if type == "annee_theorique_du_dernier_audit":
        document.annee_theorique_du_dernier_audit = value

    if type == "annee_de_realisation":
        document.annee_de_realisation = value

    if type == "criticite_issue_de_la_mission_d_audit":
        document.criticite_issue_de_la_mission_d_audit = value

    if type == "annee_de_la_prochaine_mission_d_audit":
        document.annee_de_la_prochaine_mission_d_audit = value

    document.save()
    return JsonResponse({"success":"Updated"})

def validation_plan_annuel(request):
    if request.method == 'POST':
        get_data_systeme = requests.get(listesysteme)
        get_data_processus = requests.get(listeProcessus)
        get_data_site = requests.get(listesite)
        data_systeme_list = get_data_systeme.json()
        data_processus_list = get_data_processus.json()
        data_site_list = get_data_site.json()
        get_data_filiale = requests.get(gestfiliale)
        data_filiale_list = get_data_filiale.json()
        plans_audit_annuel = []

        # Récupérer la liste des plans d'audit
        get_data = requests.get(listeplanaudit)
        planaudit_list = get_data.json()

        # Récupérer la filiale de l'utilisateur courant via la session
        idfiliale = request.session.get('idfiliale')

        # Extraire les plans d'audit de la filiale conrante
        planaudit_list = [planaudit for planaudit in planaudit_list if planaudit["idfiliale"] == idfiliale]

        # Récupérer les plans d'audit pour l'année à traiter
        annee = request.POST.get("annee")
        plans_audit_annuel = [plan for plan in planaudit_list if plan["anne_ref_cycle"] == annee]

        context = {
            'plans_audit_annuel': plans_audit_annuel,
            'data_systeme_list': data_systeme_list,
            'data_processus_list': data_processus_list,
            'data_site_list': data_site_list,
            'data_filiale_list': data_filiale_list,
            'annee_plan_audit': annee,
        }
    return render(request, "services/planaudit/validation_plan_annuel.html", context)

def selection_plan_annuel(request):
    annees_planifies = []
    # Récupérer la liste des plans d'audit
    get_data = requests.get(listeplanaudit)
    planaudit_list = get_data.json()

    # Récupérer la filiale de l'utilisateur courant via la session
    idfiliale = request.session.get('idfiliale')

    # Faire remonter les années de référence pour les plans d'audit de la filiale courante
    for plan in [planaudit for planaudit in planaudit_list if planaudit["idfiliale"] == idfiliale]:
        annee_reference = plan["anne_ref_cycle"]
        if annee_reference:
            if annee_reference.isdigit() and annee_reference not in annees_planifies:
                annees_planifies.append(annee_reference)

    context = {
        'annees_planifies': annees_planifies,
    }
    return render(request, "services/planaudit/selection_plan_annuel.html", context)

def enregistrer_plan_annuel(request):
    if request.method == "POST":
        # Récupérer la liste des plans d'audit
        get_data = requests.get(listeplanaudit)
        planaudit_list = get_data.json()

        annee_reference = request.POST.get("annee_reference")

        # Récupérer la filiale de l'utilisateur courant via la session
        idfiliale = request.session.get('idfiliale')

        # Extraire les plans d'audit de la filiale conrante
        planaudit_list = [planaudit for planaudit in planaudit_list if planaudit["idfiliale"] == idfiliale and planaudit["anne_ref_cycle"] == annee_reference]

        # Identifier les variables cochées
        for plan in planaudit_list:
            id_plan = plan["id"]
            etat_validation = request.POST.get(f"planaudit{id_plan}")
            print(etat_validation)
            if etat_validation == 'on':
                data = {
                "valid_plan": 1,
                }
                # Faire une requête POST à l'API
                response = requests.patch(f"{listeplanaudit}{id_plan}/", data=data)
                print(f"plan {id_plan} validé!")
            else:
                response = requests.delete(f"{listeplanaudit}{id_plan}")
                print("enregistrement Supprimé.")
        sweetify.success(request, f"Plan de l'année {annee_reference} validé !", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
        return redirect("services:planaudit")
    sweetify.error(request, "ÉCHEC de validation!", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
    return redirect("services:planaudit")
