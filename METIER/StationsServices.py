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

        
