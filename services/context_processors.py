import requests

from apiRessource.endpointList import get_user


def add_variable_to_Context(request):
    if  'access_token' in request.session:
        current_user = request.session.get('profile_label')
        print("This is the user Online =====>", current_user)
        currentUserEndpoint = f"{get_user}{current_user}/"
        User_instance = requests.get(currentUserEndpoint)
        theWholeUser = User_instance.json()
        username = f"{theWholeUser['nom_user']} {theWholeUser['prenom_user']}"
        userRole = theWholeUser['idprofil_user']['lib_profil_user']
        codeFiliale = theWholeUser['idfiliale']['sigle_filiale']
        return {
                'userName': username,
                'userRole': userRole,
                'codeFiliale': codeFiliale,
                'userType': theWholeUser
            }
    return {}