class StationsServices:
    def __init__(
        self,
        id_stations,
        adresse,
        ville,
        horaires,
        services,
        prixcarburants,
        coordonnees,
    ):
        self.id_stations = id_stations
        self.adresse = adresse
        self.ville = ville
        self.horaires = horaires
        self.services = services
        self.prixcarburants = prixcarburants
        self.coordonnees = coordonnees

    def __str__(self):
<<<<<<< HEAD
        return f"Station {self.id_station}: {self.nom_station}, Coordonnées GPS: {self.coordonnees_gps}"


carburant1 = TypeCarburants(1, "Essence")
prix1 = PrixCarburants(carburant1, 1.50)

horaire1 = Horaires(1, "Lundi, 10:00 - 12:00")

service1 = Services(1, "Lavage de voiture")

station = StationsServices(
    1, "Ma Station", "48.8588443, 2.2943506", [prix1], [horaire1], [service1]
)

print(station)


=======
        # Adresse et ville
        adresse_ville = f"adresse: {self.adresse}, ville: {self.ville}"

        # Horaires
        horaires_str = "horaires: "
        for jour in self.horaires.jours:
            horaires_str += f"Jour: {jour['nom']}, Ouverture: {jour['ouverture']}, Fermeture: {jour['fermeture']} | "

        # Services
        services_str = "services: "
        for service in self.services.services:
            services_str += f"{service}, "

        # Carburants
        carburants_str = "carburants: "
        for carburant in self.prixcarburants:
            carburants_str += f"Nom: {carburant.type_carburant}, Prix: {carburant.prix} | "

        # Retourne une chaîne formatée
        return f"Station {self.id_stations}: {adresse_ville}, {horaires_str}, {services_str}, {carburants_str}"
>>>>>>> aeacbe79734dfd628a13541208477f839d41be09
