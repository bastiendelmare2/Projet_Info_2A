class StationsServices:
    def __init__(
        self,
        id_stations,
        adresse,
        ville,
        services,
        prixcarburants,
        coordonnees,
    ):
        """
        Initialise une instance de StationsServices.

        Parameters
        ----------
        id_stations : int
            Identifiant de la station.
        adresse : str
            Adresse de la station.
        ville : str
            Ville où se situe la station.
        services : list
            Liste des services offerts par la station.
        prixcarburants : list
            Liste des prix des carburants disponibles à la station.
        coordonnees : Coordonnees
            Coordonnées GPS de la station.

        Attributes
        ----------
        id_stations : int
            Identifiant de la station.
        adresse : str
            Adresse de la station.
        ville : str
            Ville où se situe la station.
        services : list
            Liste des services offerts par la station.
        prixcarburants : list
            Liste des prix des carburants disponibles à la station.
        coordonnees : Coordonnees
            Coordonnées GPS de la station.
        """
        self.id_stations = id_stations
        self.adresse = adresse
        self.ville = ville
        self.services = services
        self.prixcarburants = prixcarburants
        self.coordonnees = coordonnees

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères de l'objet StationsServices.

        Returns
        -------
        str
            Chaîne représentant les détails de la station.
        """
        # Adresse et ville
        adresse_ville = f"adresse: {self.adresse}, ville: {self.ville}"

        # Services
        services_str = "services: "
        for service in self.services.services:
            services_str += f"{service}, "

        # Carburants
        carburants_str = "carburants: "
        for carburant in self.prixcarburants:
            carburants_str += f"Nom: {carburant.type_carburant}, Prix: {carburant.prix} | "

        # Retourne une chaîne formatée
        return f"Station {self.id_stations}: {adresse_ville}, {services_str}, {carburants_str}"
