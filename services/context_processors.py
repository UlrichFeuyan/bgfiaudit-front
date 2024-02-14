side_bar_admin = {
    'superuser': 'True',
    'dashbord': 'True',
    'parametre_generaux': 'True',
    'gestion_filiale': 'True',
    'profils': 'True',
    'utilisateur': 'True',
    'admin_filiale': 'True',
    'parametre_filiale': 'True',
    'gestion_filiale': 'True',
    'auditeur': 'True',
    'activite_risque': 'True',
    'document': 'True',
    'mission': 'True',
    'suivi_recommandation': 'True',
    'traitement_justif': 'True',
    'reporting_statistique': 'True',
}

side_bar_auditeur = {
    'menu_admin_filiale': 'True',
    'dashbord': 'True',
    'auditeur': 'True',
    'document': 'True',
    'activite_risque': 'True',
    'mission': 'True',
    'suivi_recommandation': 'True',
    'traitement_justif': 'True',
    'reporting_statistique': 'True',
}

side_bar_rmo = {
    'menu_rmo': 'True',
    'dashbord': 'True',
    'document': 'True',
    'suivi_recommandation': 'True',
    'traitement_justif': 'True',
    'statistique': 'True',
}

def profil_context_processor(request):
    # Récupérer le profil de l'utilisateur courant
    profil = request.session.get('profil')

    # Ajouter les informations pertinentes pour ce profil au contexte
    context = {}
    if profil:
        if profil == 'ADMIN':
            context.update(side_bar_admin)
        elif profil == 'AUDITEUR':
            context.update(side_bar_auditeur)
        elif profil == 'RMO':
            context.update(side_bar_rmo)
    context["userName"] = request.session.get('username')
    context["userRole"] = request.session.get('profil')
    return context



# def add_variable_to_Context(request):
#     if  'token' in request.session:
#         current_user = request.session.get('profil')
#         currentUserEndpoint = f"{get_user}{current_user}/"
#         User_instance = requests.get(currentUserEndpoint)
#         theWholeUser = User_instance.json()
#         username = request.session.get('code_user')
#         userRole = request.session.get('profil')
#         return {
#                 'userName': username,
#                 'userRole': userRole,
#                 'userType': theWholeUser
#             }
#     return {}