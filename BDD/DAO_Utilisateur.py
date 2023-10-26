from dao.db_connection import DBConnection
from utils.singleton import Singleton

from METIER.Utilisateur import Utilisateur


class UserDao(metaclass=Singleton):
    def ajouter_utilisateur(self, Utilisateur : Utilisateur) -> bool:
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

    def trouver_par_id(self, id) -> Utilisateur:
        """find a user by id

        Parameters
        ----------
        mail : str
            mail of the user you wish to find

        Returns
        -------
        user : User
            returns the user we're looking for by id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet2A.utilisateur               "
                        " WHERE id_utilisateur = %(id_utilisateur)s;  ",
                        {"id_utilisateur": Utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return Utilisateur


    def delete(self, Utilisateur) -> bool:
        """Deleting a user from the database

        Parameters
        ----------
        user : User
            user to be deleted from the database

        Returns
        -------
            True if the user has been correctly deleted
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Delete a user account
                    cursor.execute(
                        "DELETE FROM Projet2A.utilisateur           "
                        " WHERE id_utilisateur=%(id_utilisateur)s      ",
                        {"id_utilisateur": Utilisateur.id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0

    def se_connecter(self, id_utilisateur, mdp_utilisateur) -> Utilisateur:
        """log in with username and password
        Parameters
        ----------
        id_utilisateur : id
            identifiant
        mdp_utilisateur : str
            user password

        Returns
        -------
        Utilisateur : Utilisateur
            returns the user we're looking for
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet2A.Utilisateur               "
                        " WHERE id_utilisateur = %(id_utilisateur)s         "
                        "   AND mdp_utilisateur = %(mdp_utilisateur)s;              ",
                        {"id_utilisateur": Utilisateur.id_utilisateur,
                        "mdp_utilisateur": Utilisateur.mdp_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        return Utilisateur



    def update_mdp(self, user, new_mdp):
        """updates the mail
        Parameters
        ----------
        user : User
            user whose pass word you want to change
        new_mdp : str
            new password

        Returns
        -------
        user : User
            True if pass word has been changed
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Updates user password
                    cursor.execute(
                        "UPDATE Projet2A.utilisateur           "
                        "SET mdp_utilisateur"
                        "WHERE mdp_utilisateur=%(mdp_utilisateur)s      ",
                        {"mdp_util": new_mdp},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0