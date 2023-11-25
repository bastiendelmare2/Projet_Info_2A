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
        """Trouve les stations de service autour d'une certaine localisation géographique.

        Parameters
        ----------
        ref_latitude : float
            Latitude de la position de référence.
        ref_longitude : float
            Longitude de la position de référence.
        nom_type_carburant : str, optional
            Le type de carburant recherché, par défaut None.
        nom_service : str, optional
            Le service spécifique recherché, par défaut None.
        n : int, optional
            Nombre de stations à retourner, par défaut 3.
        distance_max : float, optional
            Distance maximale pour les stations, par défaut None.

        Returns
        -------
        tuple
            Liste des stations de service, temps de départ, informations sur la position et le nombre de stations.
        """
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
        """Trouve les stations de service autour d'une adresse utilisateur donnée.

        Parameters
        ----------
        adresse_utilisateur : str
            Adresse de l'utilisateur.
        nom_type_carburant : str, optional
            Le type de carburant recherché, par défaut None.
        nom_service : str, optional
            Le service spécifique recherché, par défaut None.
        n : int, optional
            Nombre de stations à retourner, par défaut 3.
        distance_max : float, optional
            Distance maximale pour les stations, par défaut None.

        Returns
        -------
        tuple
            Liste des stations de service, temps de départ, informations sur la position et le nombre de stations.
        """
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
        """Trouve les stations de service dans une ville donnée.

        Parameters
        ----------
        ville : str
            Nom de la ville à rechercher.
        nom_type_carburant : str, optional
            Le type de carburant recherché, par défaut None.
        nom_service : str, optional
            Le service spécifique recherché, par défaut None.

        Returns
        -------
        list
            Liste des stations de service correspondant aux critères donnés.
        """
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
        """Récupère les services et les prix de carburant pour une station préférée spécifique.

        Parameters
        ----------
        id_stations_pref : int
            Identifiant de la station préférée.

        Returns
        -------
        str or list
            Services et prix de carburant pour la station préférée.
        """
        try:
            return StationsPreferees_Dao.stations_services_par_station_preferee(id_stations_pref)
        except Exception as e:
            print("Erreur lors de la récupération des stations-services et des prix de carburant :", e)
            return json.dumps({"error": str(e)})

        
    @staticmethod
    def enlever_station_de_station_preferee(id_stations, id_stations_pref):
        """Retire une station de la liste des stations préférées.

        Parameters
        ----------
        id_stations : int
            Identifiant de la station.
        id_stations_pref : int
            Identifiant de la station préférée.

        Returns
        -------
        bool
            Résultat de l'opération de suppression.
        """

        try:
            return StationsToStationsPrefereesDAO.dissocier_station_de_station_preferee(id_stations, id_stations_pref)
        except Exception as e:
            print("Erreur lors de la dissociation de la station de la liste préférée :", e)
            return False

    @staticmethod
    def ajouter_station_a_station_preferee(id_stations, id_stations_pref):
        """Ajoute une station à la liste des stations préférées.

        Parameters
        ----------
        id_stations : int
            Identifiant de la station.
        id_stations_pref : int
            Identifiant de la station préférée.

        Returns
        -------
        bool
            Résultat de l'opération d'ajout.
        """
        try:
            return StationsToStationsPrefereesDAO.associer_station_a_station_preferee(id_stations, id_stations_pref)
        except Exception as e:
            print("Erreur lors de l'ajout de la station à la liste préférée :", e)
            return False

    @staticmethod
    def creer_station_preferee(id_compte, nom_station, id_stations_pref):
        """Crée une nouvelle station préférée pour un utilisateur.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte utilisateur.
        nom_station : str
            Nom de la station.
        id_stations_pref : int
            Identifiant de la station préférée.

        Returns
        -------
        bool
            Résultat de l'opération de création.
        """
        # Créer une nouvelle instance de StationsPreferees avec les données fournies
        nouvelle_station_pref = StationsPreferees(id_stations_pref=id_stations_pref, id_compte=id_compte, nom=nom_station)
        
        # Utiliser la méthode DAO pour ajouter cette station préférée
        return StationsPreferees_Dao.ajouter_StationsPreferee(nouvelle_station_pref)
        

    @staticmethod
    def supprimer_station_preferee(id_stations_pref):
        """Supprime une station préférée.

        Parameters
        ----------
        id_stations_pref : int
            Identifiant de la station préférée.

        Returns
        -------
        bool
            Résultat de l'opération de suppression.
        """
        # Utiliser la méthode DAO pour supprimer la station préférée
        return StationsPreferees_Dao.delete(id_stations_pref)

    @staticmethod
    def afficher_stations_preferees_utilisateur(id_compte):
        """Affiche les stations préférées d'un utilisateur.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte utilisateur.

        Returns
        -------
        dict
            Informations sur les stations préférées de l'utilisateur.
        """
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
        """Récupère tous les services disponibles.

        Returns
        -------
        list
            Liste de tous les services disponibles.
        """

        try:
            return Services_Dao.get_all_services()
        except Exception as e:
            print("Erreur lors de la récupération de tous les services :", e)
            return []

    @staticmethod
    def get_all_type_carburants():
        """Récupère tous les types de carburants disponibles.

        Returns
        -------
        list
            Liste de tous les types de carburants disponibles.
        """
        try:
            return TypeCarburantDao.get_all_type_carburants()
        except Exception as e:
            print("Erreur lors de la récupération de tous les types de carburant :", e)
            return []