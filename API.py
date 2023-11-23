# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI, Path
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette import status
import uvicorn
from SERVICES.Service_stations import Service_Station
from BDD.DAO_StationsServices import StationsServices_Dao
from SERVICES.Service_compte import ServiceCompte
from typing import Optional

# On instancie le webservice
app = FastAPI()


@app.get("/trouver/stations/plus/proche")
def stations_plus_proche_station(ref_latitude: float, ref_longitude: float, nom_type_carburant: Optional[str] = None, nom_service: Optional[str] = None, n: Optional[int] = 3, distance_max: Optional[float] = None):
    return Service_Station.trouver_stations(ref_latitude, ref_longitude,nom_type_carburant, nom_service, n, distance_max)

@app.get("/trouver/stations/plus/proche/adresse")
def stations_plus_proche_station_adresse(adresse: str, nom_type_carburant: Optional[str] = None, nom_service: Optional[str] = None, n: Optional[int] = 3, distance_max: Optional[float] = None):
    return Service_Station.trouver_stations_adresse(adresse, nom_type_carburant, nom_service, n ,distance_max)

@app.get("/stations/par/station/pref")
def stations_par_station_pref (id_stations_pref: int):
    return Service_Station.stations_services_par_station_preferee(id_stations_pref)

@app.delete("/enleve/station/de/station/pref")
def enlever_station_de_station_pref (id_stations_pref : int, id_stations: int):
    return Service_Station.enlever_station_de_station_preferee(id_stations, id_stations_pref)

@app.post("/ajouter/station/à/station/pref")
def enlever_station_a_station_pref (id_stations_pref : int, id_stations: int):
    return Service_Station.ajouter_station_a_station_preferee(id_stations, id_stations_pref)

@app.post("/créer/station/pref")
def creer_station_pref(id_compte : int, nom_station : str, id_stations_pref : int):
    return Service_Station.creer_station_preferee(id_compte, nom_station, id_stations_pref)

@app.delete("/supprimer/station/pref")
def supprimer_station_pref(id_stations_pref : int):
    return Service_Station.supprimer_station_preferee(id_stations_pref)

@app.get("/afficher/station/pref")
def afficher_station_pref(id_compte : int):
    return Service_Station.afficher_stations_preferees_utilisateur(id_compte)


# Lancement de l'application sur le port 8151
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8151)

