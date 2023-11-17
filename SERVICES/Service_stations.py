from datetime import datetime
from METIER.Coordonnees import Coordonnees
from BDD.DAO_StationsPreferees import StationsPreferees_Dao
from BDD.DAO_Stations_to_StationsPreferees import StationsToStationsPrefereesDAO
import html
import json


class Service_Station:
    @staticmethod
    def trouver_stations(liste_stations, ref_latitude, ref_longitude, n, distance_max=None):
        start_time = datetime.now()
        Coord = Coordonnees(ref_latitude, ref_longitude)
        
        for station in liste_stations:
            station.distance = Coordonnees.calculer_distance(Coord, station.coordonnees.longitude, station.coordonnees.latitude)
        
        liste_stations.sort(key=lambda x: x.distance)
        
        if distance_max is not None:
            liste_stations = [station for station in liste_stations if station.distance < distance_max]
        
        liste_stations = liste_stations[:n]
        
        unique_stations = {station.coordonnees.latitude: station for station in liste_stations}.values()
        for station in unique_stations:
            station.ville = html.unescape(station.ville)
        
        result_dict = {
            "parameters": {
                "position (longitude, latitude)": (ref_longitude, ref_latitude),
                "nombre de stations": n
            },
            "execution_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "data": [station.__dict__ for station in unique_stations]
        }
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