import math

class Coordonnees:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def calculer_distance(self, autre_coordonnee):
        # Convertir les degrés en radians
        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.radians(autre_coordonnee.latitude)
        lon2 = math.radians(autre_coordonnee.longitude)

        # Rayon de la Terre en mètres
        rayon_terre = 6371.0 * 1000  # en mètres

        # Formule de la distance haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = rayon_terre * c

        return distance.

    def str (self):
        return f"Coordonnees(latitude={self.latitude}, longitude={self.longitude})"
