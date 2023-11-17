from METIER.ComptesUtilisateurs import ComptesUtilisateurs
from BDD.DAO_Compte_Utilisateur import Compte_User_DAO



class ServiceCompte:
    @staticmethod
    def creer_compte(id_compte: int, mdp: str, identifiant: str) -> bool:
        """Crée un nouveau compte utilisateur."""
        compte = ComptesUtilisateurs(id_compte, mdp, identifiant)
        return Compte_User_DAO.ajouter_compte_utilisateur(compte_utilisateur=compte)

    @staticmethod
    def verifier_connexion(identifiant: str, mot_de_passe: str) -> bool:
        """Vérifie la connexion d'un utilisateur."""
        # Récupérer le compte utilisateur par identifiant depuis la DAO
        compte = Compte_User_DAO.get(identifiant)
        if compte:
            # Vérifier si les mots de passe correspondent
            return compte.verifier_mot_de_passe(mot_de_passe)
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