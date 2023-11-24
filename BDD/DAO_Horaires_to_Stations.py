from BDD.Connexion import DBConnection
from utils.singleton import Singleton
from METIER.StationsServices import StationsServices
from METIER.Horaires import Horaires

class HorairesToStationsDAO(metaclass=Singleton):
    def ajouter_association(self, station_id, horaire_id) -> bool:
        """Ajoute une association station-horaire dans la base de données.

        :param station_id: ID de la station.
        :type station_id: int
        :param horaire_id: ID de l'horaire.
        :type horaire_id: int
        :return: True si l'association a été créée avec succès, False sinon.
        :rtype: bool
        """
        created = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.Horaires_to_Stations(station_id, horaire_id) VALUES "
                        "(%(station_id)s, %(horaire_id)s);",
                        {
                            "station_id": station_id,
                            "horaire_id": horaire_id,
                        },
                    )
                    created = True
        except Exception as e:
            print(e)

        return created

    def supprimer_association(self, station_id, horaire_id) -> bool:
        """Supprime une association station-horaire de la base de données.

        :param station_id: ID de la station.
        :type station_id: int
        :param horaire_id: ID de l'horaire.
        :type horaire_id: int
        :return: True si l'association a été supprimée avec succès, False sinon.
        :rtype: bool
        """
        deleted = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Projet2A.Horaires_to_Stations "
                        "WHERE station_id = %(station_id)s AND horaire_id = %(horaire_id)s;",
                        {
                            "station_id": station_id,
                            "horaire_id": horaire_id,
                        },
                    )
                    deleted = True
        except Exception as e:
            print(e)

        return deleted

    def stations_ouvertes_pour_horaire(self, horaire_id):
        """Trouve toutes les stations ouvertes pour un identifiant d'horaire donné.

        :param horaire_id: ID de l'horaire.
        :type horaire_id: int
        :return: Liste des stations ouvertes pour l'identifiant d'horaire donné.
        :rtype: list
        """
        stations = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT station_id FROM Projet2A.Horaires_to_Stations WHERE horaire_id = %(horaire_id)s;",
                        {"horaire_id": horaire_id},
                    )
                    stations = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return stations

    def horaires_de_station(self, station_id):
        """Trouve les horaires d'une station donnée.

        :param station_id: ID de la station.
        :type station_id: int
        :return: Liste des horaires de la station donnée.
        :rtype: list
        """
        horaires = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT horaire_id FROM Projet2A.Horaires_to_Stations WHERE station_id = %(station_id)s;",
                        {"station_id": station_id},
                    )
                    horaires = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return horaires
