from BDD.Connexion import DBConnection
from utils.singleton import Singleton
from METIER.ComptesUtilisateurs import ComptesUtilisateurs

class Compte_User_DAO(metaclass=Singleton):
    @staticmethod
    def ajouter_compte_utilisateur(compte_utilisateur: ComptesUtilisateurs) -> bool:
        """Création d'un compte_utilisateur dans la base de données."""
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.compteutilisateur(id_compte, mdp, identifiant) VALUES "
                        "(%(id_compte)s, %(mdp)s, %(identifiant)s) RETURNING id_compte;",
                        {
                            "id_compte": compte_utilisateur.id_compte,
                            "mdp": compte_utilisateur.mot_de_passe,
                            "identifiant": compte_utilisateur.identifiant,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    @staticmethod
    def supprimer_compte_utilisateur(id_compte_utilisateur: int) -> bool:
        """Suppression d'un compte_utilisateur dans la base de données."""
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Projet2A.compteutilisateur WHERE id_compte = %(id_compte)s;",
                        {"id_compte": id_compte_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        deleted = False
        if res:
            deleted = True

        return deleted
