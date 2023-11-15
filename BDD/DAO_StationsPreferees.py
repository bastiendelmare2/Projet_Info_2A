from BDD.Connexion import DBConnection
from utils.singleton import Singleton
import json
from datetime import datetime

from METIER.StationsPreferees import StationsPreferees  # Make sure to import the correct class

class StationsPreferees_Dao(metaclass=Singleton):
    def ajouter_StationsPreferee(self, stations_pref: StationsPreferees) -> bool:
        """Ajout d'une Station Preferee dans la BDD 

        Parameters
        ----------
        stations_pref : StationsPreferees

        Returns
        -------
        created : bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.StationsPreferees(id_stations_pref, id_compte, nom) VALUES "
                        "(%(id_stations_pref)s, %(id_compte)s, %(nom)s)               "
                        "  RETURNING id_stations_pref;                                                       ",
                        {
                            "id_stations_pref": stations_pref.id_stations_pref,
                            "id_compte": stations_pref.id_compte,
                            "nom": stations_pref.nom,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    def trouver_par_id(self, id_compte) -> StationsPreferees:
        """Trouver une Station Preferee par id

        Parameters
        ----------
        id_stations_pref : int

        Returns
        -------
        stations_pref : StationsPreferees
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_stations_pref, nom                           "
                        " FROM projet2a.StationsPreferees               "
                        " WHERE id_compte = %(id_compte)s;  ",
                        {"id_compte": id_compte},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return res  # You might want to convert the result to a StationsPreferees object

    def delete(self, id_stations_pref) -> bool:
        """Deleting a station preferee from the database

        Parameters
        ----------
        id_stations_pref : int
            id of the station preferee to be deleted from the database

        Returns
        -------
        True if the station preferee has been correctly deleted
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Delete a station preferee
                    cursor.execute(
                        "DELETE FROM projet2a.StationsPreferees          "
                        " WHERE id_stations_pref=%(id_stations_pref)s      ",
                        {"id_stations_pref": id_stations_pref},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0

    def stations_services_par_station_preferee(self, id_stations_pref):
        try:
            # Ajouter la date et l'heure d'exécution
            start_time = datetime.now()

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT ss.id_stations, ss.adresse, ville,
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

            # Convertir le résultat en JSON avec ensure_ascii=False
            result_json = json.dumps(list(result_dict.values()), indent=2, default=list, ensure_ascii=False)

            # Ajouter les arguments, la date et l'heure d'exécution, et le nombre de stations dans le résultat
            result_dict = {
                "arguments": {"id_stations_pref": id_stations_pref},
                "date d'execution": start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "nombre de stations": len(result_dict),
                "data": json.loads(result_json)
            }

            return json.dumps(result_dict, indent=2, ensure_ascii=False)

        except Exception as e:
            print("Erreur lors de la récupération des stations-services et des prix de carburant :", e)
            return json.dumps({"error": str(e)})