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






############

class StationsPreferees:
    def __init__(self):
        self.listes_utilisateurs = {}  # Dictionnaire pour stocker les listes de stations par utilisateur

    def ajouter_liste(self, id_utilisateur, nom_liste):
        if id_utilisateur in self.listes_utilisateurs:
            self.listes_utilisateurs[id_utilisateur][nom_liste] = set()

    def supprimer_liste(self, id_utilisateur, nom_liste):
        if id_utilisateur in self.listes_utilisateurs and nom_liste in self.listes_utilisateurs[id_utilisateur]:
            del self.listes_utilisateurs[id_utilisateur][nom_liste]

    def ajouter_station(self, id_utilisateur, nom_liste, id_station):
        if id_utilisateur in self.listes_utilisateurs and nom_liste in self.listes_utilisateurs[id_utilisateur]:
            self.listes_utilisateurs[id_utilisateur][nom_liste].add(id_station)

    def retirer_station(self, id_utilisateur, nom_liste, id_station):
        if id_utilisateur in self.listes_utilisateurs and nom_liste in self.listes_utilisateurs[id_utilisateur]:
            self.listes_utilisateurs[id_utilisateur][nom_liste].discard(id_station)

    def __str__(self):
        result = ""
        for id_utilisateur, listes in self.listes_utilisateurs.items():
            result += f"Utilisateur: {id_utilisateur}\n"
            for nom_liste, stations in listes.items():
                result += f"  Liste: {nom_liste}, Stations: {', '.join(stations)}\n"
        return result

# Exemple d'utilisation
stations_preferees = StationsPreferees()

# Créer des listes pour un utilisateur
stations_preferees.ajouter_liste("Utilisateur1", "MaListe1")
stations_preferees.ajouter_liste("Utilisateur1", "MaListe2")

# Ajouter des stations aux listes de l'utilisateur
stations_preferees.ajouter_station("Utilisateur1", "MaListe1", "StationA")
stations_preferees.ajouter_station("Utilisateur1", "MaListe2", "StationB")

# Retirer une station de la liste de l'utilisateur
stations_preferees.retirer_station("Utilisateur1", "MaListe1", "StationA")

# Supprimer une liste de l'utilisateur
stations_preferees.supprimer_liste("Utilisateur1", "MaListe2")

# Afficher les listes de chaque utilisateur
print(stations_preferees)
