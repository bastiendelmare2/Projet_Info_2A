import pandas as pd
import json
from datetime import datetime
from METIER.Coordonnees import Coordonnees
from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.StationsServices import StationsServices


class StationsServices_Dao(metaclass=Singleton):
    def ajouter_StationsServices(StationsServices: StationsServices) -> bool:
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

    def delete(StationsServices) -> bool:
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
    
    def filtre_stations(nom_type_carburant=None, nom_service=None):
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
                    stations = cursor.fetchall()
                    stations = pd.DataFrame(stations)

            return stations

        except Exception as e:
            print("Erreur lors de la récupération des stations-services :", e)
            return []


    def trouver_stations(dataframe, ref_latitude, ref_longitude, n):
        start_time = datetime.now()  # Heure d'exécution

        dataframe['distance'] = dataframe.apply(lambda row: Coordonnees.calculer_distance(ref_latitude, ref_longitude, row['latitude'], row['longitude']), axis=1)
        dataframe = dataframe.sort_values(by='distance', ascending=True)
        dataframe = dataframe.sort_values(by='prix', ascending=True)
        dataframe = dataframe.head(n)

        # Enlever les doublons basés sur 'latitude' et 'longitude'
        dataframe = dataframe.drop_duplicates(subset=['latitude', 'longitude'])

        result_dict = {
            "parameters": {
                "position (longitude, latitude)": (ref_longitude, ref_latitude),
                "nombre de stations": n
            },
            "execution_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "data": dataframe.to_dict(orient='records')
        }
        result_dict = json.dumps(result_dict, indent=4)

        return result_dict

    def stations_services_prix_par_station_preferee(self, id_stations_pref):
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT ss.id_stations, ss.adresse, ss.ville,
                               tc.nom_type_carburants, pc.prix,
                               s.nom_service, co.longitude, co.latitude
                        FROM projet2a.Stations_to_StationsPreferees stsp
                        JOIN projet2a.StationsServices ss ON stsp.id_stations = ss.id_stations
                        LEFT JOIN projet2a.PrixCarburants pc ON ss.id_stations = pc.id_stations
                        LEFT JOIN projet2a.TypeCarburants tc ON pc.id_type_carburant = tc.id_typecarburants
                        LEFT JOIN projet2a.Stations_to_Services sts ON ss.id_stations = sts.id_stations
                        LEFT JOIN projet2a.Services s ON sts.id_service = s.id_service
                        LEFT JOIN projet2a.Coordonnees co ON ss.id_stations = co.id_stations
                        WHERE stsp.id_stations_pref = %(id_stations_pref)s
                    """, {"id_stations_pref": id_stations_pref})

                    # Récupérer les résultats
                    stations_services_prix = cursor.fetchall()

            # Créer un dictionnaire pour stocker les résultats
            result_dict = {}
            for row in stations_services_prix:
                station_id = row["id_stations"]
                if station_id not in result_dict:
                    result_dict[station_id] = {
                        "id_stations": row["id_stations"],
                        "adresse": row["adresse"],
                        "ville": row["ville"],
                        "services": set(),  # Utiliser un ensemble pour éliminer les doublons
                        "prix_carburants": set()  # Utiliser un ensemble pour éliminer les doublons
                    }

                # Ajouter les services si présents
                if row["nom_service"]:
                    result_dict[station_id]["services"].add(row["nom_service"])

                # Ajouter les prix du carburant si présents
                if row["nom_type_carburants"] and row["prix"] is not None:
                    result_dict[station_id]["prix_carburants"].add((
                        row["nom_type_carburants"],
                        row["prix"]
                    ))

            # Convertir le résultat en JSON
            result_json = json.dumps(list(result_dict.values()), indent=2, default=list)

            return result_json
        except Exception as e:
            print("Erreur lors de la récupération des stations-services et des prix de carburant :", e)
            return json.dumps({"error": str(e)})
