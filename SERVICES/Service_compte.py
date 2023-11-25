from METIER.ComptesUtilisateurs import ComptesUtilisateurs
from BDD.DAO_Compte_Utilisateur import Compte_User_DAO
import bcrypt

class ServiceCompte:
    @staticmethod
    def creer_compte(id_compte: int, mdp: str, identifiant: str) -> bool:
        """Crée un nouveau compte utilisateur.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte utilisateur.
        mdp : str
            Mot de passe du compte utilisateur.
        identifiant : str
            Identifiant unique du compte utilisateur.

        Returns
        -------
        bool
            True si le compte utilisateur a été créé avec succès, False sinon.
        """

    @staticmethod
    def verifier_connexion(id_compte: int, identifiant: str, mot_de_passe: str) -> bool:
        """Vérifie l'authentification d'un utilisateur.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte utilisateur.
        identifiant : str
            Identifiant unique du compte utilisateur.
        mot_de_passe : str
            Mot de passe du compte utilisateur.

        Returns
        -------
        bool
            True si l'authentification est réussie, False sinon.
        """

    @staticmethod
    def changer_mot_de_passe(id_compte: int, nouveau_mdp: str) -> bool:
        """Change le mot de passe d'un compte utilisateur.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte utilisateur.
        nouveau_mdp : str
            Nouveau mot de passe à définir pour le compte utilisateur.

        Returns
        -------
        bool
            True si le mot de passe a été changé avec succès, False sinon.
        """

    @staticmethod
    def supprimer_compte_utilisateur(id_compte: int, identifiant: str) -> bool:
        """Supprime un compte utilisateur.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte utilisateur.
        identifiant : str
            Identifiant unique du compte utilisateur à supprimer.

        Returns
        -------
        bool
            True si le compte utilisateur a été supprimé avec succès, False sinon.
        """
