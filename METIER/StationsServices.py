from TypeCarburants import TypeCarburants
from PrixCarburants import PrixCarburants
from Horaires import Horaires
from Services import Services


class StationsServices:
    def __init__(
        self,
        id_station,
        nom_station,
        coordonnees_gps,
        PrixCarburants,
        Horaires,
        Services,
    ):
        self.id_station = id_station
        self.nom_station = nom_station
        self.coordonnees_gps = coordonnees_gps
        self.PrixCarburants = PrixCarburants
        self.Horaires = Horaires
        self.services = Services

    def __str__(self):
        return f"Station {self.id_station}: {self.nom_station}, Coordonnées GPS: {self.coordonnees_gps}"


carburant1 = TypeCarburants(1, "Essence")
prix1 = PrixCarburants(carburant1, 1.50)

horaire1 = Horaires(1, "Lundi, 10:00 - 12:00")

service1 = Services(1, "Lavage de voiture")

station = StationsServices(
    1, "Ma Station", "48.8588443, 2.2943506", [prix1], [horaire1], [service1]
)

print(station)


