from dao.db_connection import DBConnection
from utils.singleton import Singleton

from METIER.StationsPreferees import StationsPreferees
id_stations_pref, liste_stations, utilisateur

class StationsServices_Dao(metaclass=Singleton):
    def ajouter_StationsServices(self, StationsPreferees: StationsPreferees) -> bool:
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
                        "INSERT INTO Projet2A.StationsPreferees(id_stations_pref, liste_stations) VALUES "
                        "(%(id_stations_pref)s, %(liste_stations)s)               "
                        "  RETURNING id_stations_pref;                                                       ",
                        {
                            "id_stations": StationsPreferees.id_stations_pref,
                            "liste_stations": StationsPreferees.liste_stations
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    def trouver_par_id(self, id) -> StationsPreferees:
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
                        "  FROM projet2A.StationsPreferees               "
                        " WHERE id_stations_pref = %(id_stations_pref)s;  ",
                        {"id_stations_pref": StationsPreferees.id_stations_pref},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return StationsPreferees

    def delete(self, StationsPreferees) -> bool:
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
                        "DELETE FROM Projet2A.StationsPreferees          "
                        " WHERE id_stations_pref=%(id_stations_pref)s      ",
                        {"id_stations_pref": StationsPreferees.id_stations},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0
