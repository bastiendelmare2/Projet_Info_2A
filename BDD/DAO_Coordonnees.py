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
    
    @staticmethod
    def get(id_stations) -> tuple:
        """Récupère les coordonnées d'une station par son identifiant."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_stations, longitude, latitude FROM projet2a.Coordonnees WHERE id_stations = %(id_stations)s;",
                        {"id_stations": id_stations}
                    )
                    res = cursor.fetchone()

                    if res:
                        return res  # Retourne un tuple (id_stations, longitude, latitude)
                    else:
                        return None
        except Exception as e:
            print(e)
