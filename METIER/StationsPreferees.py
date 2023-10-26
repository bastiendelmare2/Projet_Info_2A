# Import des classes
from StationsServices import StationsServices
from Utilisateur import Utilisateur
from Horaires import Horaires
from Services import Services

class StationsPreferees:
    def __init__(self, id_stations_pref, liste_stations, utilisateur):
        self.id_stations_pref = id_stations_pref
        self.liste_stations = liste_stations
        self.utilisateur = utilisateur  # Associez directement l'utilisateur

    def __str__(self):
        return f"Stations Préférées {self.id_stations_pref} de l'Utilisateur {self.utilisateur.nom_utilisateur}"

# Exemple d'utilisation de la classe StationsPreferees avec des objets StationService et Utilisateur
utilisateur = Utilisateur(123, "Nom de l'utilisateur", "prénom", 22)
horaire1 = Horaires(1, ("Lundi, 10:00 - 12:00"))
services1 = Services(4, 'laverie')

liste_stations_preferees = [
    StationsServices(
        1, "Ma Station", "48.8588443, 2.2943506", 54, [horaire1], [services1]
    )
]

stations_preferees = StationsPreferees(1, liste_stations_preferees, utilisateur)

print(stations_preferees)



