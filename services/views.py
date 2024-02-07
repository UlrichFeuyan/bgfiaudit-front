from django.shortcuts import render, redirect
import requests
from apiRessource.endpointList import signInSuperAdmin, listeFiliale, listePole, listeUtilisateur, listeProcessus, \
    listeActivite, listecontrole, listetypemission, listegraviterisk, listefamillerisk, signInAdmin


# Create your views here.
def signIn(request):
    get_filiale = requests.get(listeFiliale)
    if get_filiale.status_code == 200:
        filialeList = get_filiale.json()
        if request.method == 'POST':
            if 'filiale_btn' in request.POST:
                print("========== filiale ICI ==========")
                username = request.POST.get('username')
                password = request.POST.get('password')
                filiale = request.POST.get('filiale_id')
                print(username, password,filiale)

                # data = {
                #     "username": username,
                #     "password": password,
                #     "filiale": filiale
                # }
                # response = requests.get(signInAdmin, data)
                #
                # if response.status_code == 200:
                #     feedback = response.json()
                #     print("Everything good ", feedback)
                return redirect("services:homeAdminFiliale")

                # else:
                #     print("L'erreur est la suivante: ", response.text)
            elif 'sAdmin_btn' in request.POST:
                print("========== Admin ICI ==========")
                username = request.POST.get('username')
                password = request.POST.get('password')
                print(f"l'username est {username} et le mot de passe est {password}")
                # data = {
                #     "username": username,
                #     "password": password
                # }
                # response = requests.get(signInSuperAdmin, auth=(username, password))
                #
                # if response.status_code == 200:
                #     feedback = response.json()
                #     print("Everything good ", feedback)
                return redirect("services:home_superAdmin")

                # else:
                #     print("Le message est la suivant: ", response.text)
    else:
        print("Le message est la suivant: ", get_filiale.text)

    return render(request, 'services/signIn/signIn.html', locals())


def SuperAdmin(request):
    return render(request, 'services/index.html', locals())


def adminAsFiliale(request):
    return render(request, 'services/index_filiale.html', locals())


def gestFilialeSAdmin(request):
    get_filiale = requests.get(listeFiliale)
    print(get_filiale.json())

    filialeList = get_filiale.json()
    # else:
    #     print("Le message est ========> ",get_filiale.text)
    return render(request, 'services/liste-filiale_sAdmin.html', locals())


def gestFiliale(request):
    get_filiale = requests.get(listeFiliale)
    filialeList = get_filiale.json()
    return render(request, 'services/liste-filiale.html', locals())


def gestpole(request):
    get_filiale = requests.get(listePole)
    filialeList = get_filiale.json()
    return render(request, 'services/liste_pole.html', locals())


def gestprocessus(request):
    get_filiale = requests.get(listeProcessus)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/liste_processus.html', locals())


def gestutilisateur_spAdmin(request):
    get_filiale = requests.get(listeUtilisateur)
    filialeList = get_filiale.json()
    return render(request, 'services/liste_utilisateur.html', locals())


def gestutilisateur(request):
    get_filiale = requests.get(listeUtilisateur)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/liste_utilisateur.html', locals())


def risqueFamille(request):
    get_filiale = requests.get(listefamillerisk)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/risqueFamille.html')


def graviteRisque(request):
    get_filiale = requests.get(listegraviterisk)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/graviteRisque.html')


def typeMission(request):
    get_filiale = requests.get(listetypemission)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/typeMission.html')


def corpsControl(request):
    get_filiale = requests.get(listecontrole)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/corpsControl.html')

def activite(request):
    get_filiale = requests.get(listeActivite)
    filialeList = get_filiale.json()
    print(filialeList)
    return render(request, 'services/activite.html',locals())
