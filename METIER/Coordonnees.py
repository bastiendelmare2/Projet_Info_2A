import math
class Coordonnees:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def calculer_distance(self, x, y):
        """ Calcule la distance entre deux localisations, en fonction de leurs coordonnées 
        
        Parameters
        ----------
        autre_coordonnee : Coordonnées
            Le point de la destination dont on veut calculer la distance

        Returns
        -------
        float
            La distance entre les deux localisations en kilomètres
        """
        # Convertir les degrés en radians
        lon1 = math.radians(self.longitude)
        lat1 = math.radians(self.latitude)
        lon2 = math.radians(x)
        lat2 = math.radians(y)

        # Rayon de la Terre en kilomètres
        rayon_terre = 6371.0  # en kilomètres

        # Formule de la distance haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = rayon_terre * c

        return round(distance, 2)

