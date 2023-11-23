import schedule
import time
import threading
from fastapi import FastAPI
from Alimtentation import Alimentation
from SERVICES.Service_stations import Service_Station
from SERVICES.Service_compte import ServiceCompte
from typing import Optional
import uvicorn

class API:
    def __init__(self):
        self.app = FastAPI()

        
        @self.app.get("/trouver/stations/plus/proche")
        def stations_plus_proche_station(ref_latitude: float, ref_longitude: float, nom_type_carburant: Optional[str] = None, nom_service: Optional[str] = None, n: Optional[int] = 3, distance_max: Optional[float] = None):
            return Service_Station.trouver_stations(ref_latitude, ref_longitude,nom_type_carburant, nom_service, n, distance_max)

        @self.app.get("/trouver/stations/plus/proche/adresse")
        def stations_plus_proche_station_adresse(adresse: str, nom_type_carburant: Optional[str] = None, nom_service: Optional[str] = None, n: Optional[int] = 3, distance_max: Optional[float] = None):
            return Service_Station.trouver_stations_adresse(adresse, nom_type_carburant, nom_service, n ,distance_max)

        @self.app.get("/trouver/stations/par/ville")
        def trouver_stations_par_ville(ville: str, nom_type_carburant: Optional[str] = None, nom_service: Optional[str] = None):
            return Service_Station.trouver_stations_par_ville( ville,nom_type_carburant, nom_service)
        
        @self.app.post("/creer/compte")
        def creer_compte(id_compte: int, identifiant: str, mdp: str):
            creation = ServiceCompte.creer_compte(id_compte, mdp, identifiant)
            if creation:
                return "Le compte a bien été créé"
            else: 
                return "Le compte n'a pas été créé"
        
        @self.app.post("/changer/motdepasse")
        def changer_mot_de_passe(id_compte: int, nouveau_mdp: str):
            changement = ServiceCompte.changer_mot_de_passe(id_compte, nouveau_mdp)
            if changement: 
                return "Le mot de passe a bien été changé"
            else:
                return "Il y a eu une erreur lors du changement de votre mot de passe"
            
        @self.app.delete("/supprimer/compte")
        def supprimer_compte(id_compte : int, identifiant : str):
            suppression = ServiceCompte.supprimer_compte_utilisateur(id_compte, identifiant)
            if suppression:
                return "Le compte a bien été supprimé"
            else:
                return "echec de la suppression du compte"

        @self.app.get("/stations/par/station/pref")
        def stations_par_station_pref (id_stations_pref: int):
            return Service_Station.stations_services_par_station_preferee(id_stations_pref)

        @self.app.delete("/enleve/station/de/station/pref")
        def enlever_station_de_station_pref (id_stations_pref : int, id_stations: int):
            delete = Service_Station.enlever_station_de_station_preferee(id_stations, id_stations_pref)
            if delete:
                return "La station a bien été enelvé de votre liste"
            else:
                return "Erreur dans la suppresion"

        @self.app.post("/ajouter/station/à/station/pref")
        def enlever_station_a_station_pref (id_stations_pref : int, id_stations: int):
            ajoute = Service_Station.ajouter_station_a_station_preferee(id_stations, id_stations_pref)
            if ajoute:
                return "La station a bien été ajouté de votre liste"
            else:
                return "Erreur dans l'ajout'"

        @self.app.post("/créer/station/pref")
        def creer_station_pref(id_compte : int, nom_station : str, id_stations_pref : int):
            cree =  Service_Station.creer_station_preferee(id_compte, nom_station, id_stations_pref)
            if cree:
                return "Vous avez bien créé liste de stations préférées"
            else : 
                return "Cet identifiant de stations préférés existe déjà"

        @self.app.delete("/supprimer/station/pref")
        def supprimer_station_pref(id_stations_pref : int):
            supp = Service_Station.supprimer_station_preferee(id_stations_pref)
            if supp:
                return "Votre liste de station préféréé a bien été supprimée"

        @self.app.get("/afficher/station/pref")
        def afficher_station_pref(id_compte : int):
            return Service_Station.afficher_stations_preferees_utilisateur(id_compte)

    def renouveler_base_de_donnees(self):
        Alimentation.reset_de_la_table()

    def run(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8151)
