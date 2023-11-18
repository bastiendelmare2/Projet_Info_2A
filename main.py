from BDD.DAO_Compte_Utilisateur import Compte_User_DAO
from METIER.ComptesUtilisateurs import ComptesUtilisateurs
from SERVICES.Service_compte import ServiceCompte

print(ServiceCompte.verifier_connexion(100, "truc", "truc"))