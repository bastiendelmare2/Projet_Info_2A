from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.TypeCarburants import TypeCarburants


class UserDao(metaclass=Singleton):
    def ajouter_typecarburants(self, TypesCarburants : TypeCarburants) -> bool:
        """Creating a types_carburant in the database

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
                        "INSERT INTO Projet2A.TypesCaburants(nom) VALUES "
                        "(%(nom)s)",
                        {
                            "nom": TypeCarburants.nom
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    def trouver_par_id(self, id) -> TypeCarburants:
        """find a user by id

        Parameters
        ----------
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
                        "  FROM projet2A.TypesCarburants               "
                        " WHERE id = %(id)s;  ",
                        {"id_utilisateur": Utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return TypeCarburants


    