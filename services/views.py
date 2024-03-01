import json
import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Sum, Count
from rest_framework.response import Response
import sweetify

from apiRessource.authenticate_user import authenticate_user
from .decorators import *
from apiRessource.endpointList import *


# Create your views here.
def signIn(request):
    get_filiale = requests.get(listeFiliale)
    filialeList = get_filiale.json()
    if request.method == 'POST':
        try:
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
                    request.session['filiale'] = user_data['sigle_filiale']
                    request.session['idfiliale'] = user_data['idfiliale']

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
        except Exception as e:
            messages.error(request, f'error: {str(e)}')
    return render(request, 'services/signIn/signIn.html', locals())

@login_required_api
def homeDashboard(request):
    dashboard_active = 'True'
    return render(request, 'services/superAdmin/index.html', locals())

def gestFilialeSAdmin(request):
    get_filiale = requests.get(listeFiliale)
    print(get_filiale.json())

    filialeList = get_filiale.json()
    # else:
    #     print("Le message est ========> ",get_filiale.text)
    return render(request, 'services/superAdmin/liste-filiale_sAdmin.html', locals())

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

        # Supprimer la clé 'filiale' de la session
    if 'filiale' in request.session:
        del request.session['filiale']
    return redirect('services:signIn')

def profil(request):
    code_user = request.session.get('username')
    nom = request.session.get('nom_user')
    prenom = request.session.get('prenom_user')
    email = request.session.get('email_user')
    return render(request, 'services/signIn/profil.html', locals())

def change_password(request):
    if request.method == "POST":
        last_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        # Données à envoyer dans la requête POST
        data = {
                "last_password": last_password,
                "new_password": new_password,
                "new_password2": new_password2,
                "token": request.session['token'],
                }
        # Faire une requête POST à l'API
        response = requests.patch(f"{ges_user}change_password/", data=data)
        sweetify.info(request, "Connexion réussit!", showConfirmButton=False, timer=2000, allowOutsideClick=True, confirmButtonText="OK", toast=True, timerProgressBar=True, position="top")
        return redirect('services:profil')
    return render(request, 'services/signIn/change_password.html', locals())
