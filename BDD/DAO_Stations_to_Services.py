from BDD.Connexion import DBConnection
from utils.singleton import Singleton

class StationsToServicesDAO(metaclass=Singleton):
    @staticmethod
    def associer_station_a_service(id_stations, id_service):
        """Associe une station de service à une station préférée dans la base de données.

        Parameters
        ----------
        id_stations : int
            ID de la station de service.
        id_service : int
            ID du service associé à la station.

        Returns
        -------
        created : bool
            True si l'association a été créée avec succès, False sinon.
        """
        created = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.Stations_to_Services(id_stations, id_service) VALUES "
                        "(%(id_stations)s, %(id_service)s);",
                        {
                            "id_stations": id_stations,
                            "id_service": id_service,
                        },
                    )
                    created = True
        except Exception as e:
            print(e)

        return created
