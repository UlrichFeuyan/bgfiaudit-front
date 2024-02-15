side_bar_super_admin = {
    'menu_super_admin': 'True',
    'parametre_generaux': 'True',
    'gestion_filiale': 'True',
    'profils': 'True',
    'utilisateur': 'True',
}

side_bar_auditeur_filiale = {
    'menu_auditeur_filiale': 'True',
    'dashbord': 'True',
    'auditeur': 'True',
    'documents': 'True',
    'activite_risque': 'True',
    'mission': 'True',
    'suivi_recommandation': 'True',
    'traitement_justif': 'True',
    'reporting_statistique': 'True',
}

side_bar_rmo_filiale = {
    'menu_rmo_filiale': 'True',
    'dashbord': 'True',
    'documents': 'True',
    'suivi_recommandation': 'True',
    'traitement_justif': 'True',
    'statistique': 'True',
}

side_bar_admin_filiale = {
    'menu_admin_filiale': 'True',
    'parametre_filiale': 'True',
    'gestion_filiale': 'True',
    'utilisateur': 'True',
    'auditeur': 'True',
    'activite_risque': 'True',
    'document': 'True',
}

def profil_context_processor(request):
    # Récupérer le profil de l'utilisateur courant
    profil = request.session.get('profil')

    # Ajouter les informations pertinentes pour ce profil au contexte
    context = {}
    if profil:
        if profil == 'SUPER_ADMIN':
            context.update(side_bar_super_admin)
        elif profil == 'AUDITEUR':
            context.update(side_bar_auditeur_filiale)
        elif profil == 'RMO':
            context.update(side_bar_rmo_filiale)
        elif profil == 'ADMIN':
            context.update(side_bar_admin_filiale)
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