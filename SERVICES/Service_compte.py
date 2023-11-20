from METIER.ComptesUtilisateurs import ComptesUtilisateurs
from BDD.DAO_Compte_Utilisateur import Compte_User_DAO
import bcrypt


class ServiceCompte:
    @staticmethod
    def creer_compte(id_compte: int, mdp: str, identifiant: str) -> bool:
        """Crée un nouveau compte utilisateur."""
        compte = ComptesUtilisateurs(id_compte, mdp, identifiant)
        return Compte_User_DAO.ajouter_compte_utilisateur(compte_utilisateur=compte)

    @staticmethod
    def verifier_connexion(id_compte: int, identifiant: str, mot_de_passe: str) -> bool:
        compte_utilisateur = Compte_User_DAO.get(id_compte)

        if compte_utilisateur and compte_utilisateur.identifiant == identifiant:
            # Hachage du mot de passe entré par l'utilisateur avec le sel du compte utilisateur
            mot_de_passe_clair = mot_de_passe.encode('utf-8')
            mot_de_passe_hashe = bcrypt.hashpw(mot_de_passe_clair, compte_utilisateur.sel)

            # Vérification du mot de passe haché avec celui stocké dans la base de données
            return bcrypt.checkpw(mot_de_passe_hashe, compte_utilisateur.mot_de_passe)

        return False


    @staticmethod
    def changer_mot_de_passe(id_compte: int, nouveau_mdp: str) -> bool:
        """Change le mot de passe d'un compte utilisateur."""
        # Récupérer le compte utilisateur par ID depuis la DAO
        compte = Compte_User_DAO.get(id_compte)
        if compte:
            # Modifier le mot de passe
            compte.modifier_mot_de_passe(nouveau_mdp)
            # Mettre à jour le mot de passe dans la base de données via la DAO
            return Compte_User_DAO.modifier_mot_de_passe(compte, nouveau_mdp)
        return False