from METIER.ComptesUtilisateurs import ComptesUtilisateurs
from BDD.DAO_Compte_Utilisateur import Compte_User_DAO
from SERVICES.Service_compte import ServiceCompte


compte = Compte_User_DAO.get(22)
print(compte)