class StationsServices:
    def __init__(
        self,
        id_stations,
        adresse,
        ville
    ):
        self.id_stations = id_stations
        self.adresse = adresse
        self.ville = ville

    def __str__(self):
        return f"Station {self.id_stations}: adresse {self.adresse}, ville {self.ville}"
