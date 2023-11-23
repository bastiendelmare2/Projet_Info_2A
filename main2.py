from SERVICES.Service_stations import Service_Station
from METIER.Coordonnees import Coordonnees

coord = Coordonnees(0, 0)  # Remplacez ces valeurs par des coordonnées par défaut
coord_gps = coord.transfo_adresse_GPS("124 avenue Jean Jaurès Clamart")

print(coord_gps)

print(Service_Station.trouver_stations_adresse("124 avenue Jean Jaurès Clamart"))

