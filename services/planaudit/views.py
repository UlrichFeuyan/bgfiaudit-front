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
from django_tables2 import SingleTableView, Table
from ..models import Document
from ..tables import *
import pandas
import sweetify
import unicodedata

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

class DocumentTable(Table):
    model = Document
    columns = ('fillale', 'annee_de_reference', 'systeme', 'processus', 'site', 'criticite_issue_de_la_cartographie_des_risques', 'annee_theorique_du_dernier_audit', 'annee_de_realisation', 'criticite_issue_de_la_mission_d_audit', 'annee_de_la_prochaine_mission_d_audit')
    filter_fields = ('fillale', 'annee_de_reference', 'systeme')


class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'
    table_class = DocumentTable

    def get_queryset(self):
        df = pandas.read_excel('fichier.xlsx')
        documents = [Document(nom=row[0], fichier=row[1]) for row in df.values]
        return documents


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

def import_plan_audit(request):
    if request.method == "POST" and request.FILES.get("fichier_excel"):
        fichier_excel = request.FILES['fichier_excel']
        # Importer le fichier Excel et convertir en une liste d'objets Document

        df = pandas.read_excel(fichier_excel)
        documents = [
            Document(
                fillale=row[0],
                annee_de_reference=row[1],
                systeme=row[2],
                processus=row[3],
                site=row[4],
                criticite_issue_de_la_cartographie_des_risques=row[5],
                annee_theorique_du_dernier_audit=row[6],
                annee_de_realisation=row[7],
                criticite_issue_de_la_mission_d_audit=row[8],
                annee_de_la_prochaine_mission_d_audit=row[9],
            )
            for row in df.values
        ]
        Document.objects.bulk_create(documents)
        messages.success(request, "Les données ont été importées avec succès.")

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
    try:
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
            data = {
                    "idfiliale": [f["idfiliale"] for f in filiales if remove_accents(f["sigle_filiale"].upper())==remove_accents(filiale.upper())][0],
                    "anne_ref_cycle": annee_de_reference,
                    "idsysteme": [s["id_sys"] for s in systemes if remove_accents(s["libsys"].upper())==remove_accents(systeme.upper())][0],
                    "idprocessus": [p["idprocessus"] for p in process if remove_accents(p["libprocessus"].upper())==remove_accents(processus.upper())][0],
                    "idsite": [s["id_site"] for s in sites if remove_accents(s["lib_site"].upper())==remove_accents(site.upper())][0],
                    "criticite_carto": criticies[f"{remove_accents(criticite_issue_de_la_cartographie_des_risques.upper())}"],
                    "annee_theo_last_audit": annee_theorique_du_dernier_audit,
                    "annee_eff_last_audit": annee_de_realisation,
                    "criticite_audit": criticies[f"{remove_accents(criticite_issue_de_la_mission_d_audit.upper())}"],
                    "annee_theo_proch": annee_de_la_prochaine_mission_d_audit,
                }
            # Faire une requête POST à l'API
            response = requests.post(f"{listeplanaudit}", data=data)
    except Exception as e:
        sweetify.info(request, f"Erreur: {str(e)}", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
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