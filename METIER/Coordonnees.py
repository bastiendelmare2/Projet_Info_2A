import math

class Coordonnees:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def calculer_distance(self, autre_coordonnee):

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
        La distance entre les deux points est d'environ {distance:.2f} mètres.


        """
    
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

        return distance



# Exemple d'utilisation
point1 = Coordonnees(52.5200, 13.4050)
point2 = Coordonnees(48.8566, 2.3522)

distance = point1.calculer_distance(point2)
print(f"La distance entre les deux points est d'environ {distance:.2f} mètres.")