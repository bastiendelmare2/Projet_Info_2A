from datetime import datetime
from METIER.Coordonnees import Coordonnees
from BDD.DAO_StationsPreferees import StationsPreferees_Dao
from BDD.DAO_Stations_to_StationsPreferees import StationsToStationsPrefereesDAO
from BDD.DAO_Services import Services_Dao
from BDD.DAO_TypeCarburants import TypeCarburantDao
from METIER.StationsPreferees import StationsPreferees
from BDD.DAO_StationsServices import StationsServices_Dao
import html
import json


class Service_Station:
    def trouver_stations(ref_latitude, ref_longitude, nom_type_carburant = None, nom_service = None, n = 3, distance_max=None):  
        liste_stations = StationsServices_Dao.filtre_stations(nom_type_carburant, nom_service)
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
        
        # Créer une liste pour stocker les stations
        stations_list = []
        
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
            stations_list.append(station_info)
        
        return stations_list, start_time, {
            "position (longitude, latitude)": (ref_longitude, ref_latitude),
            "nombre de stations": n
        }

    def trouver_stations_adresse(adresse_utilisateur, nom_type_carburant=None, nom_service=None, n=3, distance_max=None):
        liste_stations = StationsServices_Dao.filtre_stations(nom_type_carburant, nom_service)
        start_time = datetime.now()
        
        # Convertir l'adresse en coordonnées GPS
        coord = Coordonnees(0, 0)  # Remplacez ces valeurs par des coordonnées par défaut
        coord_gps = coord.transfo_adresse_GPS(adresse_utilisateur)
        
        if coord_gps is None:
            return [], start_time, {"error": "Adresse non trouvée."}
        
        # Utiliser les coordonnées obtenues depuis transfo_adresse_GPS
        coord = Coordonnees(coord_gps[0], coord_gps[1])  # Utilise les coordonnées dans l'ordre (latitude, longitude)
        
        for station in liste_stations:
            station.distance = Coordonnees.calculer_distance(coord, station.coordonnees[0], station.coordonnees[1])
        
        liste_stations.sort(key=lambda x: x.distance)
        
        if distance_max is not None:
            liste_stations = [station for station in liste_stations if station.distance < distance_max]
        
        liste_stations = liste_stations[:n]
        
        for station in liste_stations:
            station.ville = html.unescape(station.ville)
        
        stations_list = []
        
        for station in liste_stations:
            station_info = {
                "id_stations": station.id_stations,
                "adresse": station.adresse,
                "ville": station.ville,
                "distance": station.distance,
                "coordonnees": station.coordonnees,
                "services": station.services,
                "prixcarburants": station.prixcarburants
            }
            stations_list.append(station_info)
        
        return stations_list, start_time, {
            "position (longitude, latitude)": adresse_utilisateur,
            "nombre de stations": n
        }


    @staticmethod
    def trouver_stations_par_ville(ville, nom_type_carburant=None, nom_service=None, ):
        try:
            liste_stations = StationsServices_Dao.filtre_stations(ville = ville, nom_type_carburant= nom_type_carburant, nom_service= nom_service)
            stations_list = []
            
            for station in liste_stations:
                # Vérifier si la ville correspond
                if ville and station.ville != ville:
                    continue
                
                station_info = {
                    "id_stations": station.id_stations,
                    "adresse": station.adresse,
                    "ville": station.ville,
                    "services": station.services,
                    "prixcarburants": station.prixcarburants
                }
                stations_list.append(station_info)
            
            return stations_list
        except Exception as e:
            print("Erreur lors de la récupération des stations-services par ville :", e)
            return []


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
        
        # Préparer la réponse avec l'identifiant de compte
        response_dict = {
            "id_compte": id_compte,
            "stations_preferees": stations_preferees
        }
        
        if not stations_preferees:
            response_dict["error"] = "Aucune station préférée trouvée pour cet utilisateur."
        
        return response_dict

    @staticmethod
    def get_all_services():
        try:
            return Services_Dao.get_all_services()
        except Exception as e:
            print("Erreur lors de la récupération de tous les services :", e)
            return []

    @staticmethod
    def get_all_type_carburants():
        try:
            return TypeCarburantDao.get_all_type_carburants()
        except Exception as e:
            print("Erreur lors de la récupération de tous les types de carburant :", e)
            return []