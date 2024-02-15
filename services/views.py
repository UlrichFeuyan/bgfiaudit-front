import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.views.generic import TemplateView, ListView

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
            data = {'code_user': code_user, 'password': password}
            response = requests.post(loginUrl, data=data)
            if response.status_code == 200:
                user_data = response.json()
                # Inclure le jeton d'accès dans l'en-tête de chaque requête ultérieure

                request.session['token'] = user_data['auth_token']
                request.session['username'] = user_data['code_user']
                request.session['profil'] = user_data['profil_user']
                return redirect('services:home_superAdmin')
            else:
                messages.error(request, 'Login failed. Please try again.')
        elif 'sAdmin_btn' in request.POST:
            if code_user == 'admin' and password == 'admin' and (filiale not in filialeList):
                request.session['token'] = "token_admin"
                request.session['username'] = 'US001'
                request.session['profil'] = 'SUPER_ADMIN'
                return redirect('services:home_superAdmin')
            else:
                messages.error(request, 'Login failed. Please try again.')
        else:
            messages.error(request, 'Login failed. Please try again.')
    return render(request, 'services/signIn/signIn.html', locals())

def login(request):
    if request.method == 'POST':
        if 'filiale_btn' in request.POST:
            print("==========  ICI Admin ==========")
            code_user = request.POST.get('username')
            password = request.POST.get('password')
            data = {'code_user': code_user, 'password': password}
            response = requests.post(loginUrl, data=data)
            if response.status_code == 200:
                user_data = response.json()
                # Inclure le jeton d'accès dans l'en-tête de chaque requête ultérieure

                request.session['token'] = user_data['auth_token']
                request.session['username'] = user_data['code_user']
                request.session['profil'] = user_data['profil_user']
                return redirect('services:home_superAdmin')
            else:
                messages.error(request, 'Login failed. Please try again.')
    return render(request, 'services/signIn/signIn.html', locals())


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

def gestions_des_filiales(request):
    gestion_filiale_active = 'True'
    return render(request, 'services/gestions_des_filiales.html', locals())

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



class RepertoireRacine(TemplateView):
    template_name = 'services/repertoire_racine.html'

    def dispatch(self, request, *args, **kwargs):
        profil = request.session.get('profil')
        if not profil == 'ADMIN':
            return redirect('services:signIn')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parametre_generaux'] = 'True'
        context['dropdown_parametre_generaux'] = 'True'
        context['active_repertoire_racine'] = 'True'
        return context

def adminAsFiliale(request):
    current_user = request.session.get('profile_label')
    print("This is the user Online =====>",current_user)
    currentUserEndpoint = f"{get_user}{current_user}/"
    User_instance = requests.get(currentUserEndpoint)
    theWholeUser = User_instance.json()
    # print(User_instance.json())
    return render(request, 'services/filiale/index_filiale.html', locals())


def gestFilialeSAdmin(request):
    get_filiale = requests.get(listeFiliale)
    print(get_filiale.json())

    filialeList = get_filiale.json()
    # else:
    #     print("Le message est ========> ",get_filiale.text)
    return render(request, 'services/superAdmin/liste-filiale_sAdmin.html', locals())


def gestFiliale(request):
    get_filiale = requests.get(listeFiliale)
    filialeList = get_filiale.json()
    return render(request, 'services/filiale/liste-filiale.html', locals())


def gestpole(request):
    get_filiale = requests.get(listePole)
    filialeList = get_filiale.json()
    return render(request, 'services/filiale/liste_pole.html', locals())


def gestprocessus(request):
    get_filiale = requests.get(listeProcessus)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/filiale/liste_processus.html', locals())


def gestutilisateur_spAdmin(request):
    get_filiale = requests.get(listeUtilisateur)
    filialeList = get_filiale.json()
    return render(request, 'services/superAdmin/liste_utilisateur_sAdmin.html', locals())


def gestutilisateur(request):
    get_filiale = requests.get(listeUtilisateur)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/filiale/liste_utilisateur.html', locals())


def risqueFamille(request):
    get_filiale = requests.get(listefamillerisk)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/superAdmin/risqueFamille.html')


def graviteRisque(request):
    get_filiale = requests.get(listegraviterisk)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/superAdmin/graviteRisque.html')


def typeMission(request):
    get_filiale = requests.get(listetypemission)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/superAdmin/typeMission.html')


def corpsControl(request):
    get_filiale = requests.get(listecontrole)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/superAdmin/corpsControl.html')


def activite(request):
    get_filiale = requests.get(listeActivite)
    filialeList = get_filiale.json()
    dropdown_activite_risque = 'True'
    activite_active = 'True'
    print(filialeList)
    return render(request, 'services/filiale/activite.html', locals())


def profileSAdmin(request):
    get_filiale = requests.get(listeprofil)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/superAdmin/profil_sAdmin.html', locals())


def settingAudit(request):
    return render(request, 'services/Audit/index_audit.html', locals())


def settingRMO(request):
    return render(request, 'services/ROM/index_rmo.html', locals())
