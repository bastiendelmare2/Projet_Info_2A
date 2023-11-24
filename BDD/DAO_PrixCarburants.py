from BDD.Connexion import DBConnection
from utils.singleton import Singleton

class PrixCarburantsDAO(metaclass=Singleton):
    @staticmethod
    def ajouter_prix_carburant(id_type_carburant, id_stations, prix):
        """Ajoute un prix de carburant dans la base de données.

        :param id_type_carburant: ID du type de carburant.
        :type id_type_carburant: int
        :param id_stations: ID de la station de service.
        :type id_stations: int
        :param prix: Prix du carburant dans la station de service.
        :type prix: float
        :return: True si le prix de carburant a été créé avec succès, False sinon.
        :rtype: bool
        """
        created = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.PrixCarburants(id_type_carburant, id_stations, prix) VALUES "
                        "(%(id_type_carburant)s, %(id_stations)s, %(prix)s);",
                        {
                            "id_type_carburant": id_type_carburant,
                            "id_stations": id_stations,
                            "prix": prix,
                        },
                    )
                    created = True
        except Exception as e:
            print(e)

        return created

    @staticmethod
    def supprimer_prix_carburant(type_carburant_id):
        """Supprime un prix de carburant de la base de données.

        :param type_carburant_id: ID du type de carburant.
        :type type_carburant_id: int
        :return: True si le prix de carburant a été supprimé avec succès, False sinon.
        :rtype: bool
        """
        deleted = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Projet2A.PrixCarburants "
                        "WHERE type_carburant_id = %(type_carburant_id)s;",
                        {
                            "type_carburant_id": type_carburant_id,
                        },
                    )
                    deleted = True
        except Exception as e:
            print(e)

        return deleted

    @staticmethod
    def prix_carburant_dans_station(id_type_carburant, id_stations):
        """Trouve le prix d'un type de carburant dans une station de service.

        :param id_type_carburant: ID du type de carburant.
        :type id_type_carburant: int
        :param id_stations: ID de la station de service.
        :type id_stations: int
        :return: Prix du type de carburant dans la station de service.
        :rtype: float
        """
        prix = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT prix FROM Projet2A.PrixCarburants WHERE id_type_carburant = %(id_type_carburant)s "
                        "AND id_stations = %(id_stations)s;",
                        {
                            "id_type_carburant": id_type_carburant,
                            "id_stations": id_stations,
                        },
                    )
                    prix = cursor.fetchone()
        except Exception as e:
            print(e)

        return prix

    @staticmethod
    def stations_service_pour_type_carburant(id_type_carburant):
        """Trouve les stations de service pour un type de carburant donné.

        :param id_type_carburant: ID du type de carburant.
        :type id_type_carburant: int
        :return: Liste des ID des stations de service offrant le type de carburant donné.
        :rtype: list
        """
        stations = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_stations FROM Projet2A.PrixCarburants WHERE id_type_carburant = %(id_type_carburant)s;",
                        {
                            "id_type_carburant": id_type_carburant,
                        },
                    )
                    stations = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return stations
