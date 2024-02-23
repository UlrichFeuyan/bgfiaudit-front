# list des url
from os.path import join

base_url = "http://127.0.0.1:8004"
# base_url = "http://137.184.83.80"

# url connexion
signInSuperAdmin = base_url + "/superuser_login/"
loginUrl = f"{base_url}/utilisateurs/login/"
logoutUrl = f"{base_url}/authentication/logout/"

signInAdmin = base_url + "/utilisateurs/login/"

# urls parametrages
listeParametrages = base_url + "/parametrages/"

# urls filiale
listeFiliale = base_url + "/filiale/"

# urls pole
listePole = base_url + "/pole/"

# urls processus
listeProcessus = base_url + "/processus/"

# urls utilisateurs
listeUtilisateur = base_url + "/utilisateurs/"

# urls activite
listeActivite = base_url + "/activites/"

# urls corpsControle
listecontrole = base_url + "/corpsdecontrole/"

# urls GraviteRisque
listegraviterisk = base_url + "/graviterisk/"

# urls risqueFamille
listefamillerisk = base_url + "/famillerisk/"

# urls typeMission
typemission = base_url + "/typemission/"

# urls typeMission
gestfiliale = base_url + "/filiale/"

# urls profils
listeprofil = base_url + "/profiluser/"

# urls profils
listeprofilauditeur = base_url + "/profilauditeur/"

# urls corpsdecontrole
corpsdecontrole = base_url + "/corpsdecontrole/"

# urls evaluations_impact_risque
evalimpactrisk = base_url + "/evalimpactrisk/"

# urls pour recuperer connecté
ges_user = f"{base_url}/utilisateurs/"

