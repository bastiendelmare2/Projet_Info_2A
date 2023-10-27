from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.PrixCarburants import PrixCarburants

class PrixCarburantsDAO(metaclass=Singleton):
    def ajouter_prix_carburant(self, type_carburant_id, station_service_id, prix):
        """Ajouter un prix de carburant dans la base de données

        Parameters
        ----------
        type_carburant_id : int
            ID du type de carburant
        station_service_id : int
            ID de la station de service
        prix : float
            Prix du carburant dans la station de service

        Returns
        -------
        created : bool
            True si le prix de carburant a été créé avec succès, False sinon
        """
        created = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.PrixCarburants(id_type_carburant, station_service_id, prix) VALUES "
                        "(%(id_type_carburant)s, %(id_stations)s, %(prix)s);",
                        {
                            "type_carburant_id": type_carburant_id,
                            "station_service_id": station_service_id,
                            "prix": prix,
                        },
                    )
                    created = True
        except Exception as e:
            print(e)

        return created

        def supprimer_prix_carburant(self, id_):
            """Supprimer un prix de carburant de la base de données

            Parameters
            ----------
            type_carburant_id : int
                ID du type de carburant
            station_service_id : int
                ID de la station de service

            Returns
            -------
            deleted : bool
                True si le prix de carburant a été supprimé avec succès, False sinon
            """
            deleted = False

            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "DELETE FROM Projet2A.PrixCarburants "
                            "WHERE type_carburant_id = %(type_carburant_id)s AND station_service_id = %(station_service_id)s;",
                            {
                                "type_carburant_id": type_carburant_id,
                                "station_service_id": station_service_id,
                            },
                        )
                        deleted = True
            except Exception as e:
                print(e)

            return deleted

    def prix_carburant_dans_station(self, id_type_carburant, id_stations):
        """Trouver le prix d'un type de carburant dans une station de service

        Parameters
        ----------
        type_carburant_id : int
            ID du type de carburant
        station_service_id : int
            ID de la station de service

        Returns
        -------
        prix : float
            Prix du type de carburant dans la station de service
        """
        prix = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT prix FROM Projet2A.PrixCarburants WHERE type_carburant_id = %(id_type_carburant)s "
                        "AND station_service_id = %(id_stations)s;",
                        {
                            "type_carburant_id": type_carburant_id,
                            "station_service_id": station_service_id,
                        },
                    )
                    prix = cursor.fetchone()
        except Exception as e:
            print(e)

        return prix

    def stations_service_pour_type_carburant(self, id_type_carburant):
        """Trouver les stations de service pour un type de carburant donné

        Parameters
        ----------
        type_carburant_id : int
            ID du type de carburant

        Returns
        -------
        stations : list
            Liste des ID des stations de service offrant le type de carburant donné
        """
        stations = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT station_service_id FROM Projet2A.PrixCarburants WHERE type_carburant_id = %(type_carburant_id)s;",
                        {
                            "type_carburant_id": type_carburant_id,
                        },
                    )
                    stations = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return stations
