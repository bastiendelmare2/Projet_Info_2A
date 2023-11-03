from BDD.Connexion import DBConnection
from utils.singleton import Singleton

class StationsServices_Dao(metaclass=Singleton):
    def ajouter_StationsServices(id_stations_pref, id_utilisateur) -> bool:
        """Ajout d'une Station Service dans la BDD 

        Parameters
        ----------
         Stations Services: StationsServices

        Returns
        -------
        created : bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.StationsPreferees(id_stations_pref, id_utilisateur) VALUES "
                        "(%(id_stations_pref)s, %(id_utilisateur)s)               "
                        "  RETURNING id_stations_pref;                                                       ",
                        {
                            "id_stations": id_stations_pref,
                            "liste_stations": id_utilisateur
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    def trouver_par_id(self, id) : 
        """Touver une STations Service par id

        Parameters
        ----------
        id : int

        Returns
        -------
        StationsServices : StationsServices

        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet2a.StationsPreferees               "
                        " WHERE id_stations_pref = %(id_stations_pref)s;  ",
                        {"id_stations_pref": id_stations_pref},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

    def delete(id_stations_pref) -> bool:
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
                        "DELETE FROM projet2a.StationsPreferees          "
                        " WHERE id_stations_pref=%(id_stations_pref)s      ",
                        {"id_stations_pref": id_stations_pref},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0

    