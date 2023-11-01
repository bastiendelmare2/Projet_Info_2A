from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.Utilisateur import Utilisateur


class UserDao(metaclass=Singleton):
    def ajouter_utilisateur( Utilisateur : Utilisateur) -> bool:
        """Creating a user in the database

        Parameters
        ----------
        user : User

        Returns
        -------
        created : bool
            True if the creation is a success
            False otherwise
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.utilisateur(nom_utilisateur, prenom_utilisateur, age_utilisateur) VALUES "
                        "(%(nom_utilisateur)s, %(prenom_utilisateur)s, %(mdp_utilisateur)s, %(age_utilisateur)s)               "
                        "  RETURNING id_utilisateur;                                                       ",
                        {
                            "id_utilisateur": Utilisateur.id_utilisateur,
                            "nom_utilisateur": Utilisateur.nom_utilisateur,
                            "prenom_utilisateur": Utilisateur.prenom_utilisateur,
                            "age_utilisateur": Utilisateur.age_utilisateur,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created