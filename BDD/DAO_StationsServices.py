import pandas as pd
import json
import html
from datetime import datetime
from METIER.Coordonnees import Coordonnees
from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.StationsServices import StationsServices


class StationsServices_Dao(metaclass=Singleton):
    def ajouter_StationsServices(self,StationsServices: StationsServices) -> bool:
        """Ajout d'une Station Service dans la BDD 

        Parameters
        ----------
         Stations Services: StationsServices

        Returns
        -------
        created : bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.StationsServices(id_stations, adresse, ville) VALUES "
                        "(%(id_stations)s, %(adresse)s, %(ville)s)               "
                        "  RETURNING id_stations;                                                       ",
                        {
                            "id_stations": StationsServices.id_stations,
                            "adresse": StationsServices.adresse,
                            "ville": StationsServices.ville,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    def trouver_par_id(self, id) -> StationsServices:
        """Touver une STations Service par id

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
                        "  FROM projet2A.StationsServices               "
                        " WHERE id_stations = %(id_stations)s;  ",
                        {"id_stations": StationsServices.id_stations},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return StationsServices

    def delete(self, StationsServices) -> bool:
        """Deleting a user from the database

        Parameters
        ----------
        user : User
            user to be deleted from the database

        Returns
        -------
            True if the user has been correctly deleted
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Delete a user account
                    cursor.execute(
                        "DELETE FROM projet2a.StationsServices          "
                        " WHERE id_stations=%(id_stations)s      ",
                        {"id_stations": StationsServices.id_stations},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0
    
    def filtre_stations(self, nom_type_carburant=None, nom_service=None):
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    query = """
                        SELECT ss.id_stations, ss.adresse, ss.ville, tc.nom_type_carburants, pc.prix, 
                        ARRAY_TO_STRING(ARRAY_AGG(s.nom_service), ', ') as nom_service, co.longitude, co.latitude
                        FROM projet2a.StationsServices ss
                        JOIN projet2a.PrixCarburants pc ON ss.id_stations = pc.id_stations
                        JOIN projet2a.TypeCarburants tc ON pc.id_type_carburant = tc.id_typecarburants
                        LEFT JOIN projet2a.Stations_to_Services sts ON ss.id_stations = sts.id_stations
                        LEFT JOIN projet2a.Services s ON sts.id_service = s.id_service
                        LEFT JOIN projet2a.Coordonnees co ON ss.id_stations = co.id_stations
                    """

                    conditions = []
                    params = {}

                    if nom_type_carburant:
                        conditions.append("tc.nom_type_carburants = %(nom_type_carburant)s")
                        params["nom_type_carburant"] = nom_type_carburant

                    if nom_service:
                        conditions.append("s.nom_service = %(nom_service)s")
                        params["nom_service"] = nom_service

                    if conditions:
                        query += " WHERE " + " AND ".join(conditions)

                    query += " GROUP BY ss.id_stations, ss.adresse, ss.ville, tc.nom_type_carburants, pc.prix, co.longitude, co.latitude"

                    cursor.execute(query, params)

                    # Récupérer les résultats
                    stations_data = cursor.fetchall()

                    # Création des objets StationsServices à partir des données récupérées
                    stations = []
                    for station_data in stations_data:
                        station = StationsServices(
                            id_stations=station_data[0],
                            adresse=station_data[1],
                            ville=station_data[2],
                            # Ajoutez d'autres attributs si nécessaire en fonction de votre classe StationsServices
                        )
                        stations.append(station)

            return stations

        except Exception as e:
            print("Erreur lors de la récupération des stations-services :", e)
            return []

        except Exception as e:
            print("Erreur lors de la récupération des stations-services :", e)
            return []


