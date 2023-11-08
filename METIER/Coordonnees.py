import math

class Coordonnees:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def calculer_distance(x, y, a, b):

        """ Calcule la distance entre deux localisations, en fonction de leur coordonnées 
        
        Parameters
        ----------
        autre_coordonnee : Coordonnées
                        Le point de la destination dont on veut calculer la distance

        Returns
        -------
        float
             La distance entre les deux localisations

        Examples
        --------

        >>> point1 = Coordonnees(52.5200, 13.4050) 
        >>> autre_coordonnee = Coordonnees(48.8566, 2.3522)
        >>> point1.calculer_distance(autre_coordonnee)
        877463.33
        """
    
        # Convertir les degrés en radians
        lon1 = math.radians(x)
        lat1 = math.radians(y)
        lon2 = math.radians(a)
        lat2 = math.radians(b)

        # Rayon de la Terre en mètres
        rayon_terre = 6371.0 * 1000  # en mètres

        # Formule de la distance haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = rayon_terre * c

        return round(distance, 2)

