from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse

from apiRessource.authenticate_user import authenticate_user
from .decorators import *
from apiRessource.endpointList import *


# Create your views here.
def signIn(request):
    if request.method == 'POST':
        if 'filiale_btn' in request.POST:
            print("==========  ICI Admin ==========")
            username = request.POST.get('username')
            password = request.POST.get('password')
            data = {'code_user': username, 'password': password}
            response = requests.post(loginUrl, data=data)
            if response.status_code == 200:
                user_data = response.json()
                # Inclure le jeton d'accès dans l'en-tête de chaque requête ultérieure

                request.session['access_token'] = user_data['auth_token']
                request.session['username'] = user_data['code_user']
                request.session['profile_label'] = user_data['idutilisateurs']
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
    return render(request, 'services/signIn/signIn.html', locals())


@login_required_api
def homeDashboard(request):

    return render(request, 'services/superAdmin/index.html', locals())


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
