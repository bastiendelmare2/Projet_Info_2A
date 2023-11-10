from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.StationsPreferees import StationsPreferees  # Make sure to import the correct class

class StationsPreferees_Dao(metaclass=Singleton):
    def ajouter_StationsPreferee(stations_pref: StationsPreferees) -> bool:
        """Ajout d'une Station Preferee dans la BDD 

        Parameters
        ----------
        stations_pref : StationsPreferees

        Returns
        -------
        created : bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.StationsPreferees(id_stations_pref, id_compte, nom) VALUES "
                        "(%(id_stations_pref)s, %(id_compte)s, %(nom)s)               "
                        "  RETURNING id_stations_pref;                                                       ",
                        {
                            "id_stations_pref": stations_pref.id_stations_pref,
                            "id_compte": stations_pref.id_compte,
                            "nom": stations_pref.nom,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    def trouver_par_id(self, id_stations_pref) -> StationsPreferees:
        """Trouver une Station Preferee par id

        Parameters
        ----------
        id_stations_pref : int

        Returns
        -------
        stations_pref : StationsPreferees
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        " FROM projet2a.StationsPreferees               "
                        " WHERE id_stations_pref = %(id_stations_pref)s;  ",
                        {"id_stations_pref": id_stations_pref},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return res  # You might want to convert the result to a StationsPreferees object

    def delete(id_stations_pref) -> bool:
        """Deleting a station preferee from the database

        Parameters
        ----------
        id_stations_pref : int
            id of the station preferee to be deleted from the database

        Returns
        -------
        True if the station preferee has been correctly deleted
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Delete a station preferee
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
