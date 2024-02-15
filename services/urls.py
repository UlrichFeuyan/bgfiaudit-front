from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
    path('login/', signIn, name='signIn'),
    path('', homeDashboard, name='home_superAdmin'),
    # path('', adminAsFiliale, name='homeAdminFiliale'),
    path('authentication/logout/', deconnexion, name='deconnexion'),

    # Paramètres généraux
    path('repertoire_racine', repertoire_racine, name='repertoire_racine'),
    path('famille_de_risques', famille_de_risques, name='famille_de_risques'),
    path('gravite_de_risques', gravite_de_risques, name='gravite_de_risques'),
    path('evaluations_impact_risque', evaluations_impact_risque, name='evaluations_impact_risque'),
    path('corps_de_controles', corps_de_controles, name='corps_de_controles'),
    path('type_de_missions', type_de_missions, name='type_de_missions'),

    path('gestions_des_filiales', gestions_des_filiales, name='gestions_des_filiales'),
    path('profils', profils, name='profils'),
    path('profil_utilisateur', profil_utilisateur, name='profil_utilisateur'),
    path('profil_auditeur', profil_auditeur, name='profil_auditeur'),
    path('utilisateurs', utilisateurs, name='utilisateurs'),
    path('parametrages_filiale', parametrages_filiale, name='parametrages_filiale'),
    path('pole', pole, name='pole'),
    path('processus', processus, name='processus'),
    path('matrice_de_competence', matrice_de_competence, name='matrice_de_competence'),
    path('catalogue_de_formation', catalogue_de_formation, name='catalogue_de_formation'),
    path('gestions_des_filiales', gestions_des_filiales, name='gestions_des_filiales'),
    path('auditeurs', auditeurs, name='auditeurs'),
    path('matrice_de_competence', matrice_de_competence, name='matrice_de_competence'),
    path('formation', formation, name='formation'),
    path('documents', documents, name='documents'),
    path('activites', activites, name='activites'),
    path('risques', risques, name='risques'),
    path('controles', controles, name='controles'),
    path('suivi_plan_de_couverture', suivi_plan_de_couverture, name='suivi_plan_de_couverture'),
    path('document', document, name='document'),
    path('categories_de_documents', categories_de_documents, name='categories_de_documents'),
    path('liste_de_documents', liste_de_documents, name='liste_de_documents'),
    path('menu_auditeur', menu_auditeur, name='menu_auditeur'),
    path('mission', mission, name='mission'),
    path('initialisation', initialisation, name='initialisation'),
    path('execution', execution, name='execution'),
    path('finalisation', finalisation, name='finalisation'),
    path('mise_a_jour_tpa', mise_a_jour_tpa, name='mise_a_jour_tpa'),
    path('suivi_des_recommandations', suivi_des_recommandations, name='suivi_des_recommandations'),
    path('transmission_justificatifs', transmission_justificatifs, name='transmission_justificatifs'),
    path('reporting', reporting, name='reporting'),
    path('statistiques', statistiques, name='statistiques'),
    path('stats', stats, name='stats'),

    # Page Utilisateur_filiale
    path('pole', gestpole, name='liste-pole'),
    path('processus', gestprocessus, name='liste-processus'),
    path('gestion-filiale_sAdmin/', gestFilialeSAdmin, name='gestion_filiale_admin'),
    path('gestion-filiale/', gestFiliale, name='gestion_filiale'),
    path('utilisateur_spAdmin/', gestutilisateur_spAdmin, name='liste-utilisateur_spAdmin'),
    path('utilisateur/', gestutilisateur, name='liste-utilisateur'),
    path('activite/', activite, name='activite'),


    #Page super Utilisateur
    path('gestion-filiale/', gestFiliale, name='gestion_filiale'),
    path('utilisateur/', gestutilisateur, name='liste-utilisateur'),
    path('risque-famille/', risqueFamille, name='risque_famille'),
    path('gravite-risque/', graviteRisque, name='gravite_risque'),
    path('type-mission/', typeMission, name='type_mission'),
    path('corps-control/', corpsControl, name='corps_control'),

    path('profil-sAdmin/', profileSAdmin, name='profil_sAdmin'),

    path('setting-Audit/', settingAudit, name='settingAudit'),
    path('setting-RMO/', settingRMO, name='settingRMO'),
]
