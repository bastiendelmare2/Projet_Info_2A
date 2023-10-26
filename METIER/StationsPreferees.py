# Import des classes
from StationsServices import StationsServices
from Horaires import Horaires
from Coordonnees import Coordonnees
from Services import Services

class StationsPreferees:
    def __init__(self, id_stations_pref, liste_stations):
        self.id_stations_pref = id_stations_pref
        self.liste_stations = liste_stations

    def __str__(self):
        return f"Stations Préférées {self.id_stations_pref}, liste : {self.liste_stations}"

# Exemple d'utilisation de la classe StationsPreferees avec des objets StationsServices
horaire1 = Horaires()
services1 = Services()
coordonnees = Coordonnees("Ma Station", "48.8588443, 2.2943506",)


liste_stations_preferees = [
    StationsServices(
        1,coordonnees, "Ma Station", "48.8588443, 2.2943506", 54, horaire1, [services1]
    )
]

stations_preferees = StationsPreferees(1, liste_stations_preferees)

print(stations_preferees)