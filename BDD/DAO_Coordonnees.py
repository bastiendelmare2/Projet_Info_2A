from BDD.Connexion import DBConnection
from utils.singleton import Singleton


class Coordonnees_Dao(metaclass=Singleton):
    def ajouter_coordonnees(self, id_stations, longitude, latitude) -> bool:
        """Ajout d'une Station Service dans la BDD

        Parameters
        ----------
         Services: Services

        Returns
        -------
        created : bool
        """,

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.Coordonnees(id_stations, longitude, latitude) VALUES "
                        "(%(id_stations)s, %(longitude)s, %(latitude)s);",
                        {
                            "id_stations": id_stations,
                            "longitude": longitude,
                            "latitude": latitude
                        },
                    )
        except Exception as e:
            print(e)
