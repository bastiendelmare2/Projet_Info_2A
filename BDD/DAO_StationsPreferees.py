from BDD.Connexion import DBConnection
from utils.singleton import Singleton
import json
from datetime import datetime

from METIER.StationsPreferees import StationsPreferees  # Assure-toi d'importer la classe correcte

class StationsPreferees_Dao(metaclass=Singleton):
    @staticmethod
    def ajouter_StationsPreferee(stations_pref: StationsPreferees) -> bool:
        """
        Ajout d'une Station Preferee dans la BDD.

        Parameters
        ----------
        stations_pref : StationsPreferees
            Instance de la station préférée à ajouter.

        Returns
        -------
        created : bool
            True si l'ajout a été effectué avec succès, False sinon.
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

    @staticmethod
    def trouver_par_id(id_compte) -> StationsPreferees:
        """
        Trouve une Station Preferee par identifiant de compte.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte associé à la station préférée.

        Returns
        -------
        stations_pref : StationsPreferees or None
            Informations de la station préférée si trouvée, sinon None.
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

    @staticmethod
    def delete(id_stations_pref) -> bool:
        """
        Supprime une station préférée de la base de données.

        Parameters
        ----------
        id_stations_pref : int
            Identifiant de la station préférée à supprimer.

        Returns
        -------
        deleted : bool
            True si la station préférée a été supprimée avec succès, False sinon.
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

    @staticmethod
    def stations_services_par_station_preferee(id_stations_pref):
        """
        Récupère les stations de services associées à une station préférée ainsi que leurs services et prix de carburants.

        Parameters
        ----------
        id_stations_pref : int
            Identifiant de la station préférée.

        Returns
        -------
        stations_list : list
            Liste des informations des stations associées à la station préférée.
        
        details : dict
            Informations supplémentaires sur la requête.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Récupérer le nom lié à la station préférée
                    cursor.execute(
                        "SELECT nom FROM projet2a.StationsPreferees WHERE id_stations_pref = %(id_stations_pref)s",
                        {"id_stations_pref": id_stations_pref}
                    )
                    station_pref_name = cursor.fetchone()["nom"]

                    # Récupérer les stations et leurs services/prix associés
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

                    stations_services_prix = cursor.fetchall()

            stations_dict = {}
            for row in stations_services_prix:
                station_id = row["id_stations"]
                if station_id not in stations_dict:
                    stations_dict[station_id] = {
                        "id_stations": row["id_stations"],
                        "adresse": row["adresse"],
                        "ville": row["ville"],
                        "services": set(),
                        "prix_carburants": set(),
                        "nom_station_preferee": station_pref_name  # Ajouter le nom de la station préférée à chaque entrée
                    }

                if row["nom_service"]:
                    stations_dict[station_id]["services"].add(row["nom_service"])

                if row["nom_type_carburants"] and row["prix"] is not None:
                    stations_dict[station_id]["prix_carburants"].add((
                        row["nom_type_carburants"],
                        row["prix"]
                    ))

            stations_list = list(stations_dict.values())

            return stations_list, {
                "arguments": {"id_stations_pref": id_stations_pref},
                "nombre_de_stations": len(stations_list)
            }

        except Exception as e:
            print("Erreur lors de la récupération des stations-services et des prix de carburant :", e)
            return {"error": str(e)}
