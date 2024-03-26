from django.urls import path
from .views import *
from .activites.views import *
from .auditeurs.views import *
from .catalogue_de_formation.views import *
from .categories_de_documents.views import *
from .controles.views import *
from .corps_de_controles.views import *
from .document.views import *
from .documents.views import *
from .evaluations_impact_risque.views import *
from .execution.views import *
from .famille_de_risques.views import *
from .filiale.views import *
from .finalisation.views import *
from .formation.views import *
from .gestions_des_filiales.views import *
from .gravite_de_risques.views import *
from .initialisation.views import *
from .liste_de_documents.views import *
from .matrice_de_competence.views import *
from .matrice_de_competence_param.views import *
from .menu_auditeur.views import *
from .mise_a_jour_tpa.views import *
from .mission.views import *
from .parametrages_filiale.views import *
from .pole.views import *
from .processus.views import *
from .profil_auditeur.views import *
from .profils.views import *
from .profil_utilisateur.views import *
from .repertoire_racine.views import *
from .reporting.views import *
from .risques.views import *
from .signIn.views import *
from .statistiques.views import *
from .stats.views import *
from .suivi_des_recommandations.views import *
from .suivi_plan_de_couverture.views import *
from .superAdmin.views import *
from .transmission_justificatifs.views import *
from .type_de_missions.views import *
from .site.views import *
from .systeme.views import *
from .sys_processus.views import *
from .utilisateurs.views import *
from .planaudit.views import *

app_name = 'services'
urlpatterns = [
    path('login/', signIn, name='signIn'),
    path('', homeDashboard, name='home_superAdmin'),
    # path('', adminAsFiliale, name='homeAdminFiliale'),
    path('gestion-filiale_sAdmin/', gestFilialeSAdmin, name='gestion_filiale_admin'),
    path('authentication/logout/', deconnexion, name='deconnexion'),
    path('profil/', profil, name='profil'),
    path('change_password/', change_password, name='change_password'),
    path('reset_password/<int:pk>', reset_password, name='reset_password'),

    # activites
    path('activites', activites, name='activites'),
    path('list_activites', list_activites, name='list_activites'),
    path('add_activites', add_activites, name='add_activites'),
    path('edit_activites/<int:pk>', edit_activites, name='edit_activites'),
    path('del_activites/<int:pk>', del_activites, name='del_activites'),

    # auditeurs
    path('auditeurs', auditeurs, name='auditeurs'),
    path('list_auditeurs', list_auditeurs, name='list_auditeurs'),
    path('add_auditeurs', add_auditeurs, name='add_auditeurs'),
    path('edit_auditeurs/<int:pk>', edit_auditeurs, name='edit_auditeurs'),
    path('del_auditeurs/<int:pk>', del_auditeurs, name='del_auditeurs'),

    # catalogue_de_formation
    path('catalogue_de_formation', catalogue_de_formation, name='catalogue_de_formation'),
    path('list_catalogue_de_formation', list_catalogue_de_formation, name='list_catalogue_de_formation'),
    path('add_catalogue_de_formation', add_catalogue_de_formation, name='add_catalogue_de_formation'),
    path('edit_catalogue_de_formation/<int:pk>', edit_catalogue_de_formation, name='edit_catalogue_de_formation'),
    path('del_catalogue_de_formation/<int:pk>', del_catalogue_de_formation, name='del_catalogue_de_formation'),

    # categories_de_documents
    path('categories_de_documents', categories_de_documents, name='categories_de_documents'),
    path('list_categories_de_documents', list_categories_de_documents, name='list_categories_de_documents'),
    path('add_categories_de_documents', add_categories_de_documents, name='add_categories_de_documents'),
    path('edit_categories_de_documents/<int:pk>', edit_categories_de_documents, name='edit_categories_de_documents'),
    path('del_categories_de_documents/<int:pk>', del_categories_de_documents, name='del_categories_de_documents'),

    # controles
    path('controles', controles, name='controles'),
    path('list_controles', list_controles, name='list_controles'),
    path('add_controles', add_controles, name='add_controles'),
    path('edit_controles/<int:pk>', edit_controles, name='edit_controles'),
    path('del_controles/<int:pk>', del_controles, name='del_controles'),

    # corps_de_controles
    path('corps_de_controles', corps_de_controles, name='corps_de_controles'),
    path('list_corps_de_controles', list_corps_de_controles, name='list_corps_de_controles'),
    path('add_corps_de_controles', add_corps_de_controles, name='add_corps_de_controles'),
    path('edit_corps_de_controles/<int:pk>', edit_corps_de_controles, name='edit_corps_de_controles'),
    path('del_corps_de_controles/<int:pk>', del_corps_de_controles, name='del_corps_de_controles'),

    # documents
    path('documents', documents, name='documents'),
    path('list_documents', list_documents, name='list_documents'),
    path('add_documents', add_documents, name='add_documents'),
    path('edit_documents/<int:pk>', edit_documents, name='edit_documents'),
    path('del_documents/<int:pk>', del_documents, name='del_documents'),

    # document

    # evaluations_impact_risque
    path('evaluations_impact_risque', evaluations_impact_risque, name='evaluations_impact_risque'),
    path('list_evaluations_impact_risque', list_evaluations_impact_risque, name='list_evaluations_impact_risque'),
    path('add_evaluations_impact_risque', add_evaluations_impact_risque, name='add_evaluations_impact_risque'),
    path('edit_evaluations_impact_risque/<int:pk>', edit_evaluations_impact_risque, name='edit_evaluations_impact_risque'),
    path('del_evaluations_impact_risque/<int:pk>', del_evaluations_impact_risque, name='del_evaluations_impact_risque'),

    # execution
    path('execution', execution, name='execution'),
    path('list_execution', list_execution, name='list_execution'),
    path('add_execution', add_execution, name='add_execution'),
    path('edit_execution/<int:pk>', edit_execution, name='edit_execution'),
    path('del_execution/<int:pk>', del_execution, name='del_execution'),

    # famille_de_risques
    path('famille_de_risques', famille_de_risques, name='famille_de_risques'),
    path('list_famille_de_risques', list_famille_de_risques, name='list_famille_de_risques'),
    path('add_famille_de_risques', add_famille_de_risques, name='add_famille_de_risques'),
    path('edit_famille_de_risques/<int:pk>', edit_famille_de_risques, name='edit_famille_de_risques'),
    path('del_famille_de_risques/<int:pk>', del_famille_de_risques, name='del_famille_de_risques'),

    # filiale

    # finalisation
    path('finalisation', finalisation, name='finalisation'),
    path('list_finalisation', list_finalisation, name='list_finalisation'),
    path('add_finalisation', add_finalisation, name='add_finalisation'),
    path('edit_finalisation/<int:pk>', edit_finalisation, name='edit_finalisation'),
    path('del_finalisation/<int:pk>', del_finalisation, name='del_finalisation'),

    # formation
    path('formation', formation, name='formation'),
    path('list_formation', list_formation, name='list_formation'),
    path('add_formation', add_formation, name='add_formation'),
    path('edit_formation/<int:pk>', edit_formation, name='edit_formation'),
    path('del_formation/<int:pk>', del_formation, name='del_formation'),

    # gestions_des_filiales
    path('gestions_des_filiales', gestions_des_filiales, name='gestions_des_filiales'),
    path('list_gestions_des_filiales', list_gestions_des_filiales, name='list_gestions_des_filiales'),
    path('add_gestions_des_filiales', add_gestions_des_filiales, name='add_gestions_des_filiales'),
    path('edit_gestions_des_filiales/<int:pk>', edit_gestions_des_filiales, name='edit_gestions_des_filiales'),
    path('del_gestions_des_filiales/<int:pk>', del_gestions_des_filiales, name='del_gestions_des_filiales'),

    # gravite_de_risques
    path('gravite_de_risques', gravite_de_risques, name='gravite_de_risques'),
    path('list_gravite_de_risques', list_gravite_de_risques, name='list_gravite_de_risques'),
    path('add_gravite_de_risques', add_gravite_de_risques, name='add_gravite_de_risques'),
    path('edit_gravite_de_risques/<int:pk>', edit_gravite_de_risques, name='edit_gravite_de_risques'),
    path('del_gravite_de_risques/<int:pk>', del_gravite_de_risques, name='del_gravite_de_risques'),

    # initialisation
    path('initialisation', initialisation, name='initialisation'),
    path('list_initialisation', list_initialisation, name='list_initialisation'),
    path('add_initialisation', add_initialisation, name='add_initialisation'),
    path('edit_initialisation/<int:pk>', edit_initialisation, name='edit_initialisation'),
    path('del_initialisation/<int:pk>', del_initialisation, name='del_initialisation'),

    # liste_de_documents

    # matrice_de_competence
    path('matrice_de_competence', matrice_de_competence, name='matrice_de_competence'),
    path('list_matrice_de_competence', list_matrice_de_competence, name='list_matrice_de_competence'),
    path('add_matrice_de_competence', add_matrice_de_competence, name='add_matrice_de_competence'),
    path('edit_matrice_de_competence/<int:pk>', edit_matrice_de_competence, name='edit_matrice_de_competence'),
    path('del_matrice_de_competence/<int:pk>', del_matrice_de_competence, name='del_matrice_de_competence'),

    # matrice_de_competence_param
    path('matrice_de_competence_param', matrice_de_competence_param, name='matrice_de_competence_param'),
    path('list_matrice_de_competence_param', list_matrice_de_competence_param, name='list_matrice_de_competence_param'),
    path('add_matrice_de_competence_param', add_matrice_de_competence_param, name='add_matrice_de_competence_param'),
    path('edit_matrice_de_competence_param/<int:pk>', edit_matrice_de_competence_param, name='edit_matrice_de_competence_param'),
    path('del_matrice_de_competence_param/<int:pk>', del_matrice_de_competence_param, name='del_matrice_de_competence_param'),

    # menu_auditeur

    # mise_a_jour_tpa
    path('mise_a_jour_tpa', mise_a_jour_tpa, name='mise_a_jour_tpa'),
    path('list_mise_a_jour_tpa', list_mise_a_jour_tpa, name='list_mise_a_jour_tpa'),
    path('add_mise_a_jour_tpa', add_mise_a_jour_tpa, name='add_mise_a_jour_tpa'),
    path('edit_mise_a_jour_tpa/<int:pk>', edit_mise_a_jour_tpa, name='edit_mise_a_jour_tpa'),
    path('del_mise_a_jour_tpa/<int:pk>', del_mise_a_jour_tpa, name='del_mise_a_jour_tpa'),

    # mission
    path('mission', mission, name='mission'),
    path('list_mission', list_mission, name='list_mission'),
    path('add_mission', add_mission, name='add_mission'),
    path('edit_mission/<int:pk>', edit_mission, name='edit_mission'),
    path('del_mission/<int:pk>', del_mission, name='del_mission'),

    # parametrages_filiale

    # pole
    path('pole', pole, name='pole'),
    path('list_pole', list_pole, name='list_pole'),
    path('add_pole', add_pole, name='add_pole'),
    path('edit_pole/<int:pk>', edit_pole, name='edit_pole'),
    path('del_pole/<int:pk>', del_pole, name='del_pole'),

    # processus
    path('processus', processus, name='processus'),
    path('list_processus', list_processus, name='list_processus'),
    path('add_processus', add_processus, name='add_processus'),
    path('edit_processus/<int:pk>', edit_processus, name='edit_processus'),
    path('del_processus/<int:pk>', del_processus, name='del_processus'),

    # profil_auditeur
    path('profil_auditeur', profil_auditeur, name='profil_auditeur'),
    path('list_profil_auditeur', list_profil_auditeur, name='list_profil_auditeur'),
    path('add_profil_auditeur', add_profil_auditeur, name='add_profil_auditeur'),
    path('edit_profil_auditeur/<int:pk>', edit_profil_auditeur, name='edit_profil_auditeur'),
    path('del_profil_auditeur/<int:pk>', del_profil_auditeur, name='del_profil_auditeur'),

    # profils

    # profil_utilisateur
    path('profil_utilisateur', profil_utilisateur, name='profil_utilisateur'),
    path('list_profil_utilisateur', list_profil_utilisateur, name='list_profil_utilisateur'),
    path('add_profil_utilisateur', add_profil_utilisateur, name='add_profil_utilisateur'),
    path('edit_profil_utilisateur/<int:pk>', edit_profil_utilisateur, name='edit_profil_utilisateur'),
    path('del_profil_utilisateur/<int:pk>', del_profil_utilisateur, name='del_profil_utilisateur'),

    # repertoire_racine
    path('repertoire_racine', repertoire_racine, name='repertoire_racine'),
    path('list_repertoire_racine', list_repertoire_racine, name='list_repertoire_racine'),
    path('edit_repertoire_racine/<int:pk>', edit_repertoire_racine, name='edit_repertoire_racine'),

    # reporting
    path('reporting', reporting, name='reporting'),
    path('list_reporting', list_reporting, name='list_reporting'),
    path('add_reporting', add_reporting, name='add_reporting'),
    path('edit_reporting/<int:pk>', edit_reporting, name='edit_reporting'),
    path('del_reporting/<int:pk>', del_reporting, name='del_reporting'),

    # risques
    path('risques', risques, name='risques'),
    path('list_risques', list_risques, name='list_risques'),
    path('add_risques', add_risques, name='add_risques'),
    path('edit_risques/<int:pk>', edit_risques, name='edit_risques'),
    path('del_risques/<int:pk>', del_risques, name='del_risques'),

    # signIn

    # statistiques
    path('statistiques', statistiques, name='statistiques'),
    path('list_statistiques', list_statistiques, name='list_statistiques'),
    path('add_statistiques', add_statistiques, name='add_statistiques'),
    path('edit_statistiques/<int:pk>', edit_statistiques, name='edit_statistiques'),
    path('del_statistiques/<int:pk>', del_statistiques, name='del_statistiques'),

    # stats
    path('stats', stats, name='stats'),
    path('list_stats', list_stats, name='list_stats'),
    path('add_stats', add_stats, name='add_stats'),
    path('edit_stats/<int:pk>', edit_stats, name='edit_stats'),
    path('del_stats/<int:pk>', del_stats, name='del_stats'),

    # suivi_des_recommandations
    path('suivi_des_recommandations', suivi_des_recommandations, name='suivi_des_recommandations'),
    path('list_suivi_des_recommandations', list_suivi_des_recommandations, name='list_suivi_des_recommandations'),
    path('add_suivi_des_recommandations', add_suivi_des_recommandations, name='add_suivi_des_recommandations'),
    path('edit_suivi_des_recommandations/<int:pk>', edit_suivi_des_recommandations, name='edit_suivi_des_recommandations'),
    path('del_suivi_des_recommandations/<int:pk>', del_suivi_des_recommandations, name='del_suivi_des_recommandations'),

    # suivi_plan_de_couverture
    path('suivi_plan_de_couverture', suivi_plan_de_couverture, name='suivi_plan_de_couverture'),
    path('list_suivi_plan_de_couverture', list_suivi_plan_de_couverture, name='list_suivi_plan_de_couverture'),
    path('add_suivi_plan_de_couverture', add_suivi_plan_de_couverture, name='add_suivi_plan_de_couverture'),
    path('edit_suivi_plan_de_couverture/<int:pk>', edit_suivi_plan_de_couverture, name='edit_suivi_plan_de_couverture'),
    path('del_suivi_plan_de_couverture/<int:pk>', del_suivi_plan_de_couverture, name='del_suivi_plan_de_couverture'),

    # superAdmin

    # transmission_justificatifs
    path('transmission_justificatifs', transmission_justificatifs, name='transmission_justificatifs'),
    path('list_transmission_justificatifs', list_transmission_justificatifs, name='list_transmission_justificatifs'),
    path('add_transmission_justificatifs', add_transmission_justificatifs, name='add_transmission_justificatifs'),
    path('edit_transmission_justificatifs/<int:pk>', edit_transmission_justificatifs, name='edit_transmission_justificatifs'),
    path('del_transmission_justificatifs/<int:pk>', del_transmission_justificatifs, name='del_transmission_justificatifs'),

    # type_de_missions
    path('type_de_missions', type_de_missions, name='type_de_missions'),
    path('list_type_de_missions', list_type_de_missions, name='list_type_de_missions'),
    path('add_type_de_missions', add_type_de_missions, name='add_type_de_missions'),
    path('edit_type_de_missions/<int:pk>', edit_type_de_missions, name='edit_type_de_missions'),
    path('del_type_de_missions/<int:pk>', del_type_de_missions, name='del_type_de_missions'),

    # site
    path('site', site, name='site'),
    path('list_site', list_site, name='list_site'),
    path('add_site', add_site, name='add_site'),
    path('edit_site/<int:pk>', edit_site, name='edit_site'),
    path('del_site/<int:pk>', del_site, name='del_site'),

    # plan d'audit
    path('planaudit', planaudit, name='planaudit'),
    path('list_planaudit', list_planaudit, name='list_planaudit'),
    path('add_planaudit', add_planaudit, name='add_planaudit'),
    path('edit_planaudit/<int:pk>', edit_planaudit, name='edit_planaudit'),
    path('del_planaudit/<int:pk>', del_planaudit, name='del_planaudit'),

    path('import_plan_audit', import_plan_audit, name='import_plan_audit'),
    path('upload_plan_audit', upload_plan_audit, name='upload_plan_audit'),
    path('save_document_plan_adit', save_document_plan_adit, name='save_document_plan_adit'),
    path('validation_plan_audit', validationPlanAuditListView.as_view(), name='validation_plan_audit'),
    path('validation_plan_annuel', validation_plan_annuel, name='validation_plan_annuel'),
    path('selection_plan_annuel', selection_plan_annuel, name='selection_plan_annuel'),
    path('enregistrer_plan_annuel', enregistrer_plan_annuel, name='enregistrer_plan_annuel'),
    path('list_planannuel', list_planannuel, name='list_planannuel'),

    # systeme
    path('systeme', systeme, name='systeme'),
    path('list_systeme', list_systeme, name='list_systeme'),
    path('add_systeme', add_systeme, name='add_systeme'),
    path('edit_systeme/<int:pk>', edit_systeme, name='edit_systeme'),
    path('del_systeme/<int:pk>', del_systeme, name='del_systeme'),

    path('detail_processus_systeme/<int:pk>', detail_processus_systeme, name='detail_processus_systeme'),

    # sys_processus
    path('sys_processus', sys_processus, name='sys_processus'),
    path('list_sys_processus', list_sys_processus, name='list_sys_processus'),
    path('add_sys_processus', add_sys_processus, name='add_sys_processus'),
    path('edit_sys_processus/<int:pk>', edit_sys_processus, name='edit_sys_processus'),
    path('del_sys_processus/<int:pk>', del_sys_processus, name='del_sys_processus'),

    # utilisateurs
    path('utilisateurs', utilisateurs, name='utilisateurs'),
    path('list_utilisateurs', list_utilisateurs, name='list_utilisateurs'),
    path('add_utilisateurs', add_utilisateurs, name='add_utilisateurs'),
    path('edit_utilisateurs/<int:pk>', edit_utilisateurs, name='edit_utilisateurs'),
    path('del_utilisateurs/<int:pk>', del_utilisateurs, name='del_utilisateurs'),
]
