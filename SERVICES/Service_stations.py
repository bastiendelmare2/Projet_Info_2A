from datetime import datetime
from METIER.Coordonnees import Coordonnees
from BDD.DAO_StationsPreferees import StationsPreferees_Dao
from BDD.DAO_Stations_to_StationsPreferees import StationsToStationsPrefereesDAO
from METIER.StationsPreferees import StationsPreferees
import html
import json


class Service_Station:
    @staticmethod
    def trouver_stations(liste_stations, ref_latitude, ref_longitude, n, distance_max=None):
        start_time = datetime.now()
        Coord = Coordonnees(ref_latitude, ref_longitude)
        
        for station in liste_stations:
            station.distance = Coordonnees.calculer_distance(Coord, station.coordonnees[0], station.coordonnees[1])
        
        liste_stations.sort(key=lambda x: x.distance)
        
        if distance_max is not None:
            liste_stations = [station for station in liste_stations if station.distance < distance_max]
        
        liste_stations = liste_stations[:n]
        
        for station in liste_stations:
            station.ville = html.unescape(station.ville)
            
        result_dict = {
            "parameters": {
                "position (longitude, latitude)": (ref_longitude, ref_latitude),
                "nombre de stations": n
            },
            "execution_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "data": []
        }
        
        for station in liste_stations:
            station_info = {
                "id_stations": station.id_stations,
                "adresse": station.adresse,
                "ville": station.ville,
                "distance": station.distance,
                "coordonnees": station.coordonnees,
                "services": station.services,
                "prixcarburants": station.prixcarburants  # La structure a été modifiée ici
            }
            result_dict["data"].append(station_info)
        
        result_dict = json.dumps(result_dict, indent=4, ensure_ascii=False)
        
        return result_dict




    @staticmethod
    def stations_services_par_station_preferee(id_stations_pref):
        try:
            return StationsPreferees_Dao.stations_services_par_station_preferee(id_stations_pref)
        except Exception as e:
            print("Erreur lors de la récupération des stations-services et des prix de carburant :", e)
            return json.dumps({"error": str(e)})

        
    @staticmethod
    def enlever_station_de_station_preferee(id_stations, id_stations_pref):
        try:
            return StationsToStationsPrefereesDAO.dissocier_station_de_station_preferee(id_stations, id_stations_pref)
        except Exception as e:
            print("Erreur lors de la dissociation de la station de la liste préférée :", e)
            return False

    @staticmethod
    def ajouter_station_a_station_preferee(id_stations, id_stations_pref):
        try:
            return StationsToStationsPrefereesDAO.associer_station_a_station_preferee(id_stations, id_stations_pref)
        except Exception as e:
            print("Erreur lors de l'ajout de la station à la liste préférée :", e)
            return False

    @staticmethod
    def creer_station_preferee(id_compte, nom_station, id_stations_pref):
        # Créer une nouvelle instance de StationsPreferees avec les données fournies
        nouvelle_station_pref = StationsPreferees(id_stations_pref=id_stations_pref, id_compte=id_compte, nom=nom_station)
        
        # Utiliser la méthode DAO pour ajouter cette station préférée
        return StationsPreferees_Dao.ajouter_StationsPreferee(nouvelle_station_pref)

    @staticmethod
    def supprimer_station_preferee(id_stations_pref):
        # Utiliser la méthode DAO pour supprimer la station préférée
        return StationsPreferees_Dao.delete(id_stations_pref)

    @staticmethod
    def afficher_stations_preferees_utilisateur(id_compte):
        # Utiliser la méthode DAO pour trouver toutes les stations préférées de l'utilisateur
        stations_preferees = StationsPreferees_Dao.trouver_par_id(id_compte)
        
        # Préparer la réponse JSON avec l'identifiant de compte
        response_dict = {
            "id_compte": id_compte,
            "stations_preferees": stations_preferees
        }
        
        # Convertir les résultats en un format JSON
        result_json = json.dumps(response_dict, indent=2) if stations_preferees else json.dumps({"error": "Aucune station préférée trouvée pour cet utilisateur.", "id_compte": id_compte})
        
        return result_json