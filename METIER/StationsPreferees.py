# Import des classes
from StationsServices import StationsServices
from Utilisateur import Utilisateur


class StationsPreferees:
    def __init__(self, id_stations_pref, liste_stations):
        self.id_stations_pref = id_stations_pref
        self.liste_stations = liste_stations
        self.utilisateur = None  # L'utilisateur n'est pas encore associé

    def associer_utilisateur(self, utilisateur):
        self.utilisateur = utilisateur

    def __str__(self):
        return f"Stations Préférées {self.id_stations_pref} de l'Utilisateur {self.utilisateur.nom_utilisateur}"


# Exemple d'utilisation de la classe StationsPreferees avec des objets StationService et Utilisateur
utilisateur = Utilisateur(123, "Nom de l'utilisateur")
liste_stations_preferees = [
    StationsServices(
        1, "Ma Station", "48.8588443, 2.2943506", [prix1], [horaire1], [service1]
    )
]

stations_preferees = StationsPreferees(1, liste_stations_preferees, utilisateur)

print(stations_preferees)