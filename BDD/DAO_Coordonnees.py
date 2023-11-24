from BDD.Connexion import DBConnection
from utils.singleton import Singleton

class Coordonnees_Dao(metaclass=Singleton):
    @staticmethod
    def ajouter_coordonnees(id_stations, longitude, latitude) -> bool:
        """Ajoute des coordonnées de station dans la base de données.

        :param id_stations: Identifiant de la station.
        :type id_stations: int
        :param longitude: Coordonnée longitude de la station.
        :type longitude: float
        :param latitude: Coordonnée latitude de la station.
        :type latitude: float
        :return: True si l'ajout a réussi, False sinon.
        :rtype: bool
        """
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
                    return True
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    def get(id_stations) -> tuple:
        """Récupère les coordonnées d'une station par son identifiant.

        :param id_stations: Identifiant de la station à récupérer.
        :type id_stations: int
        :return: Tuple contenant les coordonnées de la station (id_stations, longitude, latitude) ou None si non trouvé.
        :rtype: tuple or None
        """
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
            return None
