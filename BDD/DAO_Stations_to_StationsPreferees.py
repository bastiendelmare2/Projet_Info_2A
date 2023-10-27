from BDD.Connexion import DBConnection
from utils.singleton import Singleton

class StationsToStationsPrefereesDAO(metaclass=Singleton):
    def associer_station_a_station_preferee(self, id_stations, id_stations_pref) -> bool:
        """Associer une station de service à une station préférée dans la base de données

        Parameters
        ----------
        id_stations : int
            ID de la station de service
        station_preferee_id : int
            ID de la station préférée

        Returns
        -------
        created : bool
            True si l'association a été créée avec succès, False sinon
        """
        created = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.Stations_to_StationsPreferees(id_stations, id_stations_pref) VALUES "
                        "(%(id_stations)s, %(id_stations_pref)s);",
                        {
                            "id_stations": id_stations,
                            "id_stations_pref": id_stations_pref,
                        },
                    )
                    created = True
        except Exception as e:
            print(e)

        return created

    def dissocier_station_de_station_preferee(self, id_stations, id_stations_pref) -> bool:
        """Dissocier une station de service d'une station préférée dans la base de données

        Parameters
        ----------
        station_service_id : int
            ID de la station de service
        id_stations_pref : int
            ID de la station préférée

        Returns
        -------
        deleted : bool
            True si l'association a été supprimée avec succès, False sinon
        """
        deleted = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Projet2A.Stations_to_StationsPreferees "
                        "WHERE id_stations = %(id_stations)s AND id_stations_pref = %(id_stations_pref)s;",
                        {
                            "id_stations": id_stations,
                            "id_stations_pref": id_stations_pref,
                        },
                    )
                    deleted = True
        except Exception as e:
            print(e)

        return deleted

    def stations_service_de_station_preferee(self, sid_stations_pref):
        """Trouver les stations de service associées à une station préférée

        Parameters
        ----------
        station_preferee_id : int
            ID de la station préférée

        Returns
        -------
        stations_service : list
            Liste des ID des stations de service associées à la station préférée
        """
        stations_service = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_stations FROM Projet2A.Stations_to_StationsPreferees WHERE id_stations_pref = %(id_stations_pref)s;",
                        {
                            "id_stations": id_stations,
                        },
                    )
                    stations_service = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return stations_service

    def stations_preferees_de_station_service(self, id_stations):
        """Trouver les stations préférées associées à une station de service

        Parameters
        ----------
        station_service_id : int
            ID de la station de service

        Returns
        -------
        stations_preferees : list
            Liste des ID des stations préférées associées à la station de service
        """
        stations_preferees = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_stations_pref FROM Projet2A.Stations_to_StationsPreferees WHERE id_stations = %(id_stations)s;",
                        {
                            "id_stations_pref": id_stations_pref,
                        },
                    )
                    stations_preferees = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return stations_preferees
