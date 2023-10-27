from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.Services import Services


class Services_Dao(metaclass=Singleton):
    def ajouter_services(Services: Services) -> bool:
        """Ajout d'une Station Service dans la BDD

        Parameters
        ----------
         Services: Services

        Returns
        -------
        created : bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.Services(services) VALUES "
                        "(%(services)s)",
                        {
                            "services": Services.services,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    def trouver_par_id(id) -> Services:
        """Touver une Stations Service par id

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
                        "  FROM projet2a.StationsServices               "
                        " WHERE id_stations = %(id_stations)s;  ",
                        {"id_stations": Services.id_services},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return Services