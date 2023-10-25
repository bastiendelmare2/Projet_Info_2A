from StationsPreferees import StationsPreferees


class Utilisateur:
    def __init__(
        self,
        id_utilisateur,
        nom_utilisateur,
        prenom_utilisateur,
        age,
        liste_stations_preferees,
    ):
        self.id_utilisateur = id_utilisateur
        self.nom_utilisateur = nom_utilisateur
        self.prenom_utilisateur = prenom_utilisateur
        self.age = age
        self.liste_stations_preferees = liste_stations_preferees

    def associer_stations_preferees(self, stations_preferees):
        self.liste_stations_preferees.append(stations_preferees)
        stations_preferees.associer_utilisateur(
            self
        )  # Associer cette instance d'utilisateur à la liste de stations préférées

    def __str__(self):
        return f"Utilisateur {self.id_utilisateur}: {self.prenom_utilisateur} {self.nom_utilisateur}"


# Exemple d'utilisation de la classe Utilisateur avec une liste de stations préférées


# Créez des objets StationsPreferees pour la liste d'attributs id_stations_pref
stations_preferees1 = StationsPreferees(1, [1, 2, 3])
stations_preferees2 = StationsPreferees(2, [4, 5, 6])

# Créez un objet Utilisateur avec les stations préférées
utilisateur = Utilisateur(
    123,
    "Nom de l'utilisateur",
    "Prénom de l'utilisateur",
    30,
    [stations_preferees1, stations_preferees2],
)

print(utilisateur)