import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count
from django.views.generic import TemplateView, ListView
import sweetify

from apiRessource.authenticate_user import authenticate_user
from .decorators import *
from apiRessource.endpointList import *


# Create your views here.
def signIn(request):
    get_filiale = requests.get(listeFiliale)
    filialeList = get_filiale.json()
    if request.method == 'POST':
        code_user = request.POST.get('username')
        password = request.POST.get('password')
        filiale = request.POST.get('filiale_id')
        if 'filiale_btn' in request.POST:
            data = {'username': code_user, 'password': password, 'idfiliale': int(filiale)}
            response = requests.post(loginUrl, data=data)
            if response.status_code == 200:
                reponse = response.json()
                user_data = reponse['user']
                # Inclure le jeton d'accès dans l'en-tête de chaque requête ultérieure

                request.session['token'] = user_data['auth_token']
                request.session['username'] = user_data['code_user']
                request.session['profil'] = user_data['idprofil_user']

                request.session['nom_user'] = user_data['nom_user']
                request.session['prenom_user'] = user_data['prenom_user']
                request.session['email_user'] = user_data['email_user']
                sweetify.info(request, "Connexion réussit!", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
                return redirect('services:home_superAdmin')
            else:
                messages.error(request, 'Login failed. Please try again.')
        elif 'sAdmin_btn' in request.POST:
            if code_user == 'admin' and password == 'admin' and (filiale not in filialeList):
                request.session['token'] = "token_admin"
                request.session['username'] = 'US001'
                request.session['profil'] = 'SUPER_ADMIN'
                sweetify.info(request, "Connexion réussit!", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
                return redirect('services:home_superAdmin')
            else:
                messages.error(request, 'Login failed. Please try again.')
        else:
            messages.error(request, 'Login failed. Please try again.')
    return render(request, 'services/signIn/signIn.html', locals())

def profil(request):
    code_user = request.session.get('username')
    nom = request.session.get('nom_user')
    prenom = request.session.get('prenom_user')
    email = request.session.get('email_user')
    return render(request, 'services/signIn/profil.html', locals())

def change_password(request):
    # Données à envoyer dans la requête POST
    data = {
            "last_password": "last_password",
            "new_password": "new_password",
            }
    # Faire une requête POST à l'API
    response = requests.patch(f"{ges_user}", data=data)
    return render(request, 'services/signIn/change_password.html', locals())

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
    return render(request, "services/singIn/reset_password_utilisateurs.html", locals())

def deconnexion(request):
    response = requests.post(logoutUrl)
    if 'access_token' in request.session:
        del request.session['access_token']

        # Supprimer la clé 'username' de la session
    if 'username' in request.session:
        del request.session['username']

        # Supprimer la clé 'profile_label' de la session
    if 'profile_label' in request.session:
        del request.session['profile_label']
    return redirect('services:signIn')


def repertoire_racine(request):
    dropdown_parametre_generaux = 'True'
    repertoire_racine_active = 'True'
    return render(request, 'services/repertoire_racine.html', locals())

def famille_de_risques(request):
    dropdown_parametre_generaux = 'True'
    famille_risque_active = 'True'
    return render(request, 'services/famille_de_risques.html', locals())

def gravite_de_risques(request):
    dropdown_parametre_generaux = 'True'
    gravite_risque_active = 'True'
    return render(request, 'services/gravite_de_risques.html', locals())

def evaluations_impact_risque(request):
    dropdown_parametre_generaux = 'True'
    evaluation_impact_risque_active = 'True'
    return render(request, 'services/evaluations_impact_risque.html', locals())

def corps_de_controles(request):
    dropdown_parametre_generaux = 'True'
    corps_control_active = 'True'
    return render(request, 'services/corps_de_controles.html', locals())

def type_de_missions(request):
    dropdown_parametre_generaux = 'True'
    type_mission_active = 'True'
    return render(request, 'services/type_de_missions.html', locals())

def gestions_des_filiales(request):
    gestion_filiale_active = 'True'
    return render(request, 'services/gestions_des_filiales.html', locals())

def profils(request):
    dropdown_profils = 'True'
    profile_utilisdropdown_profilsateur_active = 'True'
    return render(request, 'services/profils.html', locals())

def profil_utilisateur(request):
    profile_utilisateur_active = 'True'
    dropdown_profils = 'True'
    return render(request, 'services/profil_utilisateur.html', locals())

def profil_auditeur(request):
    profile_auditeur_active = 'True'
    dropdown_profils = 'True'
    return render(request, 'services/profil_auditeur.html', locals())

def utilisateurs(request):
    utilisateurs_active = 'True'
    return render(request, 'services/utilisateurs.html', locals())

def parametrages_filiale(request):
    return render(request, 'services/parametrages_filiale.html', locals())

def pole(request):
    dropdown_parametre_filiale = 'True'
    pole_active = 'True'
    return render(request, 'services/pole.html', locals())

def processus(request):
    dropdown_parametre_filiale = 'True'
    processus_active = 'True'
    return render(request, 'services/processus.html', locals())

def matrice_de_competence(request):
    dropdown_parametre_filiale = 'True'
    matrice_competence_active = 'True'
    return render(request, 'services/matrice_de_competence.html', locals())

def catalogue_de_formation(request):
    dropdown_parametre_filiale = 'True'
    catalogue_formation_active = 'True'
    return render(request, 'services/catalogue_de_formation.html', locals())

def auditeurs(request):
    return render(request, 'services/auditeurs.html', locals())

def matrice_de_competence(request):
    dropdown_auditeur = 'True'
    matrice_competence_active = 'True'
    return render(request, 'services/matrice_de_competence.html', locals())

def formation(request):
    dropdown_auditeur = 'True'
    formation_active = 'True'
    return render(request, 'services/formation.html', locals())

def documents(request):
    documents_active = 'True'
    return render(request, 'services/documents.html', locals())

def activites(request):
    dropdown_activite_risque = 'True'
    activite_active = 'True'
    return render(request, 'services/activites.html', locals())

def risques(request):
    dropdown_activite_risque = 'True'
    risque_active = 'True'
    return render(request, 'services/risques.html', locals())

def controles(request):
    dropdown_activite_risque = 'True'
    controle_active = 'True'
    return render(request, 'services/controles.html', locals())

def suivi_plan_de_couverture(request):
    dropdown_activite_risque = 'True'
    suivi_plan_couverture_active = 'True'
    return render(request, 'services/controles.html', locals())

def document(request):
    return render(request, 'services/documents.html', locals())

def categories_de_documents(request):
    dropdown_document = 'True'
    categorie_document_active = 'True'
    return render(request, 'services/categories_de_documents.html', locals())

def liste_de_documents(request):
    dropdown_document = 'True'
    liste_document_active = 'True'
    return render(request, 'services/liste_de_documents.html', locals())

def menu_auditeur(request):
    return render(request, 'services/menu_auditeur.html', locals())

def mission(request):
    return render(request, 'services/mission.html', locals())

def initialisation(request):
    dropdown_mission = 'True'
    initialisation_active = 'True'
    return render(request, 'services/initialisation.html', locals())

def execution(request):
    dropdown_mission = 'True'
    execution_active = 'True'
    return render(request, 'services/execution.html', locals())

def finalisation(request):
    dropdown_mission = 'True'
    finalisation_active = 'True'
    return render(request, 'services/finalisation.html', locals())

def mise_a_jour_tpa(request):
    dropdown_mission = 'True'
    mise_a_jour_tpa_active = 'True'
    return render(request, 'services/mise_a_jour_tpa.html', locals())

def suivi_des_recommandations(request):
    suivi_recommandation_active = 'True'
    return render(request, 'services/suivi_des_recommandations.html', locals())

def transmission_justificatifs(request):
    transmission_justif_active = 'True'
    return render(request, 'services/transmission_justificatifs.html', locals())

def reporting(request):
    dropdown_reporting_statistique = 'True'
    reporting_active = 'True'
    return render(request, 'services/reporting.html', locals())

def statistiques(request):
    dropdown_reporting_statistique = 'True'
    statistique_active = 'True'
    return render(request, 'services/statistiques.html', locals())

def stats(request):
    stats_active = 'True'
    return render(request, 'services/statistiques.html', locals())








# class RepertoireRacine(TemplateView):
#     template_name = 'services/repertoire_racine.html'

#     def dispatch(self, request, *args, **kwargs):
#         profil = request.session.get('profil')
#         if not profil == 'ADMIN':
#             return redirect('services:signIn')
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['parametre_generaux'] = 'True'
#         context['dropdown_parametre_generaux'] = 'True'
#         context['active_repertoire_racine'] = 'True'
#         return context

# def adminAsFiliale(request):
#     current_user = request.session.get('profile_label')
#     print("This is the user Online =====>",current_user)
#     currentUserEndpoint = f"{ges_user}{current_user}/"
#     User_instance = requests.get(currentUserEndpoint)
#     theWholeUser = User_instance.json()
#     # print(User_instance.json())
#     return render(request, 'services/filiale/index_filiale.html', locals())

def gestFilialeSAdmin(request):
    get_filiale = requests.get(listeFiliale)
    print(get_filiale.json())

    filialeList = get_filiale.json()
    # else:
    #     print("Le message est ========> ",get_filiale.text)
    return render(request, 'services/superAdmin/liste-filiale_sAdmin.html', locals())





def list_repertoire_racine(request):
    get_data = requests.get(listeParametrages)
    data_list = get_data.json()
    return render(request, 'services/lists/list_repertoire_racine.html', locals())

def list_famille_de_risques(request):
    get_data = requests.get(listefamillerisk)
    data_list = get_data.json()
    return render(request, "services/lists/list_famille_de_risques.html", locals())

def list_gravite_de_risques(request):
    get_data = requests.get(listegraviterisk)
    data_list = get_data.json()
    return render(request, "services/lists/list_gravite_de_risques.html", locals())

def list_evaluations_impact_risque(request):
    get_data = requests.get(evalimpactrisk)
    data_list = get_data.json()
    return render(request, "services/lists/list_evaluations_impact_risque.html", locals())

def list_corps_de_controles(request):
    get_data = requests.get(corpsdecontrole)
    data_list = get_data.json()
    return render(request, "services/lists/list_corps_de_controles.html", locals())

def list_type_de_missions(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_type_de_missions.html", locals())

def list_profils(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_profils.html", locals())

def list_profil_utilisateur(request):
    get_data = requests.get(listeprofil)
    data_list = get_data.json()
    return render(request, "services/lists/list_profil_utilisateur.html", locals())

def list_profil_auditeur(request):
    get_data = requests.get(listeprofilauditeur)
    data_list = get_data.json()
    return render(request, "services/lists/list_profil_auditeur.html", locals())

def list_utilisateurs(request):
    get_data = requests.get(ges_user)
    data_list = get_data.json()
    return render(request, "services/lists/list_utilisateurs.html", locals())

def list_parametrages_filiale(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_parametrages_filiale.html", locals())

def list_pole(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_pole.html", locals())

def list_processus(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_processus.html", locals())

def list_matrice_de_competence(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_matrice_de_competence.html", locals())

def list_catalogue_de_formation(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_catalogue_de_formation.html", locals())

def list_gestions_des_filiales(request):
    get_data = requests.get(gestfiliale)
    data_list = get_data.json()
    return render(request, "services/lists/list_gestions_des_filiales.html", locals())

def list_auditeurs(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_auditeurs.html", locals())

def list_matrice_de_competence(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_matrice_de_competence.html", locals())

def list_formation(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_formation.html", locals())

def list_documents(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_documents.html", locals())

def list_activites(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_activites.html", locals())

def list_risques(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_risques.html", locals())

def list_controles(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_controles.html", locals())

def list_suivi_plan_de_couverture(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_suivi_plan_de_couverture.html", locals())

def list_document(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_document.html", locals())

def list_categories_de_documents(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_categories_de_documents.html", locals())

def list_liste_de_documents(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_liste_de_documents.html", locals())

def list_menu_auditeur(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_menu_auditeur.html", locals())

def list_mission(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_mission.html", locals())

def list_initialisation(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_initialisation.html", locals())

def list_execution(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_execution.html", locals())

def list_finalisation(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_finalisation.html", locals())

def list_mise_a_jour_tpa(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_mise_a_jour_tpa.html", locals())

def list_suivi_des_recommandations(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_suivi_des_recommandations.html", locals())

def list_transmission_justificatifs(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_transmission_justificatifs.html", locals())

def list_reporting(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_reporting.html", locals())

def list_statistiques(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_statistiques.html", locals())

def list_stats(request):
    get_data = requests.get(typemission)
    data_list = get_data.json()
    return render(request, "services/lists/list_stats.html", locals())











@login_required_api
def homeDashboard(request):

    return render(request, 'services/superAdmin/index.html', locals())

class Dashboard(TemplateView):
    template_name = 'services/superAdmin/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # evenements = 'Evenements.objects.all()'
        # context['nombre_transaction'] = evenements.count()

        # context['nombre_transaction_attente'] = evenements.filter(etaFin="0").count()
        # context['nombre_transaction_valide'] = evenements.filter(etaFin="1").count()
        # context['nombre_transaction_rejete'] = evenements.filter(etaFin="2").count()

        # context['nombre_versement'] = evenements.filter(natOrig="VERSP").count()
        # context['nombre_virement'] = evenements.filter(natOrig="VRT").count()
        # context['nombre_cheque'] = evenements.filter(natOrig="CHQ").count()

        # context['montant_total'] = evenements.filter(etaFin="1").aggregate(Sum('montant'))['montant__sum']

        # context['evenements'] = evenements

        # context['montants'] = 'Evenements'.objects.values_list('montant', flat=True)

        # # Récupérer tous les événements triés par date et heure
        # evenements_chronologiques = 'Evenements.objects.all()'.order_by('dcoOrig', 'hsaiOrig')

        # # Initialiser une liste pour stocker les montants dans l'ordre chronologique
        # montants_chronologiques = []
        # nums = []

        # # Parcourir chaque événement et extraire le montant
        # for evenement in evenements_chronologiques:
        #     # Combinaison de la date et de l'heure pour obtenir un objet datetime complet
        #     # date_str = evenement.dcoOrig + ' ' + evenement.hsaiOrig
        #     # date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        #     # Extraire le montant de l'événement et l'ajouter à la liste
        #     if evenement.montant:
        #         montants_chronologiques.append(evenement.montant)
        #         nums.append(" ")

        # context['montants_chronologiques'] = montants_chronologiques
        # context['nums'] = nums

        # # permet d'afficher l'option Dashboard dans menu latéral
        # context['dashbord'] = 'True'
        # context['dashbord_active'] = 'True'
        return context

def edit_repertoire_racine(request, pk):
    get_famillerisk = requests.get(f"{listeParametrages}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('racine_rep')
         # Données à envoyer dans la requête POST
        data = {
                "racine_rep": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{listeParametrages}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/modals/form_repertoire_racine.html", locals())

def edit_famille_de_risques(request, pk):
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
    return render(request, "services/modals/form_famille_de_risques.html", locals())

def edit_gravite_de_risques(request, pk):
    get_famillerisk = requests.get(f"{listegraviterisk}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libgraviterisk": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listegraviterisk}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/modals/form_gravite_de_risques.html", locals())

def edit_evaluations_impact_risque(request, pk):
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
    return render(request, "services/modals/form_evaluations_impact_risque.html", locals())

def edit_corps_de_controles(request, pk):
    get_famillerisk = requests.get(f"{listecontrole}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libcorpsdecontrole": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listecontrole}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/modals/form_corps_de_controles.html", locals())

def edit_type_de_missions(request, pk):
    get_famillerisk = requests.get(f"{typemission}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libtypemiss": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{typemission}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/modals/form_type_de_missions.html", locals())

def edit_gestions_des_filiales(request, pk):
    get_famillerisk = requests.get(f"{gestfiliale}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        sigle_filiale = request.POST.get('sigle_filiale')
        nom_filiale = request.POST.get('nom_filiale')
        pays_filiale = request.POST.get('pays_filiale')
        dg_filiale = request.POST.get('dg_filiale')
        adresse_filiale = request.POST.get('adresse_filiale')
         # Données à envoyer dans la requête POST
        data = {
                "sigle_filiale": sigle_filiale,
                "nom_filiale": nom_filiale,
                "pays_filiale": pays_filiale,
                "dg_filiale": dg_filiale,
                "adresse_filiale": adresse_filiale,
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
    return render(request, "services/modals/form_gestions_des_filiales.html", locals())

def edit_profils(request, pk):
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
    return render(request, "services/modals/form_profils.html", locals())

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
    return render(request, "services/modals/form_profil_utilisateur.html", locals())

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
    return render(request, "services/modals/form_profil_auditeur.html", locals())

def edit_utilisateurs(request, pk):
    get_filiale = requests.get(listeFiliale)
    get_profil = requests.get(listeprofil)
    filialeList = get_filiale.json()
    profilList = get_profil.json()
    get_user = requests.get(f"{ges_user}{pk}")
    data = get_user.json()
    if request.method == "POST":
        code_user = request.POST.get('code_user')
        nom_user = request.POST.get('nom_user')
        prenom_user = request.POST.get('prenom_user')
        email_user = request.POST.get('email_user')
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
                "username": code_user,
                "code_user": code_user,
                "nom_user": nom_user,
                "prenom_user": prenom_user,
                "email_user": email_user,
                "idprofil_user": f"{profil_data}",
                "idfiliale": filiale_data,
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
    return render(request, "services/modals/form_utilisateurs.html", locals())

def edit_parametrages_filiale(request, pk):
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
    return render(request, "services/modals/form_parametrages_filiale.html", locals())

def edit_pole(request, pk):
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
    return render(request, "services/modals/form_pole.html", locals())

def edit_processus(request, pk):
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
    return render(request, "services/modals/form_processus.html", locals())

def edit_matrice_de_competence(request, pk):
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
    return render(request, "services/modals/form_matrice_de_competence.html", locals())

def edit_catalogue_de_formation(request, pk):
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
    return render(request, "services/modals/form_catalogue_de_formation.html", locals())

def edit_auditeurs(request, pk):
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
    return render(request, "services/modals/form_auditeurs.html", locals())

def edit_matrice_de_competence(request, pk):
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
    return render(request, "services/modals/form_matrice_de_competence.html", locals())

def edit_formation(request, pk):
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
    return render(request, "services/modals/form_formation.html", locals())

def edit_documents(request, pk):
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
    return render(request, "services/modals/form_documents.html", locals())

def edit_activites(request, pk):
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
    return render(request, "services/modals/form_activites.html", locals())

def edit_risques(request, pk):
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
    return render(request, "services/modals/form_risques.html", locals())

def edit_controles(request, pk):
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
    return render(request, "services/modals/form_controles.html", locals())

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
    return render(request, "services/modals/form_suivi_plan_de_couverture.html", locals())

def edit_document(request, pk):
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
    return render(request, "services/modals/form_document.html", locals())

def edit_categories_de_documents(request, pk):
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
    return render(request, "services/modals/form_categories_de_documents.html", locals())

def edit_liste_de_documents(request, pk):
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
    return render(request, "services/modals/form_liste_de_documents.html", locals())

def edit_menu_auditeur(request, pk):
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
    return render(request, "services/modals/form_menu_auditeur.html", locals())

def edit_mission(request, pk):
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
    return render(request, "services/modals/form_mission.html", locals())

def edit_initialisation(request, pk):
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
    return render(request, "services/modals/form_initialisation.html", locals())

def edit_execution(request, pk):
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
    return render(request, "services/modals/form_execution.html", locals())

def edit_finalisation(request, pk):
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
    return render(request, "services/modals/form_finalisation.html", locals())

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
    return render(request, "services/modals/form_mise_a_jour_tpa.html", locals())

def edit_suivi_des_recommandations(request, pk):
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
    return render(request, "services/modals/form_suivi_des_recommandations.html", locals())

def edit_transmission_justificatifs(request, pk):
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
    return render(request, "services/modals/form_transmission_justificatifs.html", locals())

def edit_reporting(request, pk):
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
    return render(request, "services/modals/form_reporting.html", locals())

def edit_statistiques(request, pk):
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
    return render(request, "services/modals/form_statistiques.html", locals())

def edit_stats(request, pk):
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
    return render(request, "services/modals/form_stats.html", locals())



# class RepertoireRacine(TemplateView):
#     template_name = 'services/repertoire_racine.html'

#     def dispatch(self, request, *args, **kwargs):
#         profil = request.session.get('profil')
#         if not profil == 'ADMIN':
#             return redirect('services:signIn')
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['parametre_generaux'] = 'True'
#         context['dropdown_parametre_generaux'] = 'True'
#         context['active_repertoire_racine'] = 'True'
#         return context

# def adminAsFiliale(request):
#     current_user = request.session.get('profile_label')
#     print("This is the user Online =====>",current_user)
#     currentUserEndpoint = f"{ges_user}{current_user}/"
#     User_instance = requests.get(currentUserEndpoint)
#     theWholeUser = User_instance.json()
#     # print(User_instance.json())
#     return render(request, 'services/filiale/index_filiale.html', locals())


# def gestFilialeSAdmin(request):
#     get_filiale = requests.get(listeFiliale)
#     print(get_filiale.json())

#     filialeList = get_filiale.json()
#     # else:
#     #     print("Le message est ========> ",get_filiale.text)
#     return render(request, 'services/superAdmin/liste-filiale_sAdmin.html', locals())


def add_famille_de_risques(request):
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
    return render(request, "services/modals/form_famille_de_risques.html", locals())

def add_gravite_de_risques(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libgraviterisk": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listegraviterisk}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/modals/form_gravite_de_risques.html", locals())

def add_evaluations_impact_risque(request):
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
    return render(request, "services/modals/form_evaluations_impact_risque.html", locals())

def add_corps_de_controles(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libcorpsdecontrole": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listecontrole}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/modals/form_corps_de_controles.html", locals())

def add_type_de_missions(request):
    if request.method == "POST":
        value = request.POST.get('libfamillerisk')
         # Données à envoyer dans la requête POST
        data = {
                "libtypemiss": f"{value}"
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{typemission}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/modals/form_type_de_missions.html", locals())

def add_gestions_des_filiales(request):
    if request.method == "POST":
        sigle_filiale = request.POST.get('sigle_filiale')
        nom_filiale = request.POST.get('nom_filiale')
        pays_filiale = request.POST.get('pays_filiale')
        dg_filiale = request.POST.get('dg_filiale')
        adresse_filiale = request.POST.get('adresse_filiale')
         # Données à envoyer dans la requête POST
        data = {
                "sigle_filiale": sigle_filiale,
                "nom_filiale": nom_filiale,
                "pays_filiale": pays_filiale,
                "dg_filiale": dg_filiale,
                "adresse_filiale": adresse_filiale,
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
    return render(request, "services/modals/form_gestions_des_filiales.html", locals())

def add_profils(request):
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
    return render(request, "services/modals/form_profils.html", locals())

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
    return render(request, "services/modals/form_profil_utilisateur.html", locals())

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
    return render(request, "services/modals/form_profil_auditeur.html", locals())

def add_utilisateurs(request):
    get_filiale = requests.get(listeFiliale)
    get_profil = requests.get(listeprofil)
    filialeList = get_filiale.json()
    profilList = get_profil.json()
    if request.method == "POST":
        code_user = request.POST.get('code_user')
        nom_user = request.POST.get('nom_user')
        prenom_user = request.POST.get('prenom_user')
        email_user = request.POST.get('email_user')
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
                "username": code_user,
                "code_user": code_user,
                "nom_user": nom_user,
                "prenom_user": prenom_user,
                "email_user": email_user,
                "idprofil_user": profil_data,
                "idfiliale": filiale_data,
                "password": "",
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
    return render(request, "services/modals/form_utilisateurs.html", locals())

def add_parametrages_filiale(request):
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
    return render(request, "services/modals/form_parametrages_filiale.html", locals())

def add_pole(request):
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
    return render(request, "services/modals/form_pole.html", locals())

def add_processus(request):
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
    return render(request, "services/modals/form_processus.html", locals())

def add_matrice_de_competence(request):
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
    return render(request, "services/modals/form_matrice_de_competence.html", locals())

def add_catalogue_de_formation(request):
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
    return render(request, "services/modals/form_catalogue_de_formation.html", locals())

def add_auditeurs(request):
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
    return render(request, "services/modals/form_auditeurs.html", locals())

def add_matrice_de_competence(request):
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
    return render(request, "services/modals/form_matrice_de_competence.html", locals())

def add_formation(request):
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
    return render(request, "services/modals/form_formation.html", locals())

def add_documents(request):
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
    return render(request, "services/modals/form_documents.html", locals())

def add_activites(request):
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
    return render(request, "services/modals/form_activites.html", locals())

def add_risques(request):
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
    return render(request, "services/modals/form_risques.html", locals())

def add_controles(request):
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
    return render(request, "services/modals/form_controles.html", locals())

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
    return render(request, "services/modals/form_suivi_plan_de_couverture.html", locals())

def add_document(request):
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
    return render(request, "services/modals/form_document.html", locals())

def add_categories_de_documents(request):
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
    return render(request, "services/modals/form_categories_de_documents.html", locals())

def add_liste_de_documents(request):
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
    return render(request, "services/modals/form_liste_de_documents.html", locals())

def add_menu_auditeur(request):
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
    return render(request, "services/modals/form_menu_auditeur.html", locals())

def add_mission(request):
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
    return render(request, "services/modals/form_mission.html", locals())

def add_initialisation(request):
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
    return render(request, "services/modals/form_initialisation.html", locals())

def add_execution(request):
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
    return render(request, "services/modals/form_execution.html", locals())

def add_finalisation(request):
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
    return render(request, "services/modals/form_finalisation.html", locals())

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
    return render(request, "services/modals/form_mise_a_jour_tpa.html", locals())

def add_suivi_des_recommandations(request):
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
    return render(request, "services/modals/form_suivi_des_recommandations.html", locals())

def add_transmission_justificatifs(request):
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
    return render(request, "services/modals/form_transmission_justificatifs.html", locals())

def add_reporting(request):
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
    return render(request, "services/modals/form_reporting.html", locals())

def add_statistiques(request):
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
    return render(request, "services/modals/form_statistiques.html", locals())

def add_stats(request):
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
    return render(request, "services/modals/form_stats.html", locals())





# class RepertoireRacine(TemplateView):
#     template_name = 'services/repertoire_racine.html'

#     def dispatch(self, request, *args, **kwargs):
#         profil = request.session.get('profil')
#         if not profil == 'ADMIN':
#             return redirect('services:signIn')
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['parametre_generaux'] = 'True'
#         context['dropdown_parametre_generaux'] = 'True'
#         context['active_repertoire_racine'] = 'True'
#         return context

# def adminAsFiliale(request):
#     current_user = request.session.get('profile_label')
#     print("This is the user Online =====>",current_user)
#     currentUserEndpoint = f"{ges_user}{current_user}/"
#     User_instance = requests.get(currentUserEndpoint)
#     theWholeUser = User_instance.json()
#     # print(User_instance.json())
#     return render(request, 'services/filiale/index_filiale.html', locals())


# def gestFilialeSAdmin(request):
#     get_filiale = requests.get(listeFiliale)
#     print(get_filiale.json())

#     filialeList = get_filiale.json()
#     # else:
#     #     print("Le message est ========> ",get_filiale.text)
#     return render(request, 'services/superAdmin/liste-filiale_sAdmin.html', locals())






def del_famille_de_risques(request, pk):
    get_famillerisk = requests.get(f"{listefamillerisk}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listefamillerisk}{pk}")
        # sweetify.info(request, "Enregistrement supprimé", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/del/del_famille_de_risques.html", locals())

def del_gravite_de_risques(request, pk):
    get_famillerisk = requests.get(f"{listegraviterisk}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listegraviterisk}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/del/del_gravite_de_risques.html", locals())

def del_evaluations_impact_risque(request, pk):
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
    return render(request, "services/del/del_evaluations_impact_risque.html", locals())

def del_corps_de_controles(request, pk):
    get_famillerisk = requests.get(f"{listecontrole}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listecontrole}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/del/del_corps_de_controles.html", locals())

def del_type_de_missions(request, pk):
    get_famillerisk = requests.get(f"{typemission}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{typemission}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/del/del_type_de_missions.html", locals())

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
    return render(request, "services/del/del_gestions_des_filiales.html", locals())

def del_profils(request, pk):
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
    return render(request, "services/del/del_profils.html", locals())

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
    return render(request, "services/del/del_profil_utilisateur.html", locals())

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
    return render(request, "services/del/del_profil_auditeur.html", locals())

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
    return render(request, "services/del/del_utilisateurs.html", locals())

def del_parametrages_filiale(request, pk):
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
    return render(request, "services/del/del_parametrages_filiale.html", locals())

def del_pole(request, pk):
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
    return render(request, "services/del/del_pole.html", locals())

def del_processus(request, pk):
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
    return render(request, "services/del/del_processus.html", locals())

def del_matrice_de_competence(request, pk):
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
    return render(request, "services/del/del_matrice_de_competence.html", locals())

def del_catalogue_de_formation(request, pk):
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
    return render(request, "services/del/del_catalogue_de_formation.html", locals())

def del_auditeurs(request, pk):
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
    return render(request, "services/del/del_auditeurs.html", locals())

def del_matrice_de_competence(request, pk):
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
    return render(request, "services/del/del_matrice_de_competence.html", locals())

def del_formation(request, pk):
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
    return render(request, "services/del/del_formation.html", locals())

def del_documents(request, pk):
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
    return render(request, "services/del/del_documents.html", locals())

def del_activites(request, pk):
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
    return render(request, "services/del/del_activites.html", locals())

def del_risques(request, pk):
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
    return render(request, "services/del/del_risques.html", locals())

def del_controles(request, pk):
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
    return render(request, "services/del/del_controles.html", locals())

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
    return render(request, "services/del/del_suivi_plan_de_couverture.html", locals())

def del_document(request, pk):
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
    return render(request, "services/del/del_document.html", locals())

def del_categories_de_documents(request, pk):
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
    return render(request, "services/del/del_categories_de_documents.html", locals())

def del_liste_de_documents(request, pk):
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
    return render(request, "services/del/del_liste_de_documents.html", locals())

def del_menu_auditeur(request, pk):
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
    return render(request, "services/del/del_menu_auditeur.html", locals())

def del_mission(request, pk):
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
    return render(request, "services/del/del_mission.html", locals())

def del_initialisation(request, pk):
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
    return render(request, "services/del/del_initialisation.html", locals())

def del_execution(request, pk):
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
    return render(request, "services/del/del_execution.html", locals())

def del_finalisation(request, pk):
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
    return render(request, "services/del/del_finalisation.html", locals())

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
    return render(request, "services/del/del_mise_a_jour_tpa.html", locals())

def del_suivi_des_recommandations(request, pk):
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
    return render(request, "services/del/del_suivi_des_recommandations.html", locals())

def del_transmission_justificatifs(request, pk):
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
    return render(request, "services/del/del_transmission_justificatifs.html", locals())

def del_reporting(request, pk):
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
    return render(request, "services/del/del_reporting.html", locals())

def del_statistiques(request, pk):
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
    return render(request, "services/del/del_statistiques.html", locals())

def del_stats(request, pk):
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
    return render(request, "services/del/del_stats.html", locals())
