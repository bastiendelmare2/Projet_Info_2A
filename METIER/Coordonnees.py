import math
from geopy.geocoders import Nominatim

class Coordonnees:
    def __init__(self, latitude, longitude):
        """Initialise les coordonnées géographiques.

        Parameters
        ----------
        latitude : float
            La latitude de la localisation.
        longitude : float
            La longitude de la localisation.
        """
        self.latitude = latitude
        self.longitude = longitude

    def calculer_distance(self, x, y):
        """Calcule la distance entre deux localisations en kilomètres.

        Parameters
        ----------
        x : float
            La latitude de la destination.
        y : float
            La longitude de la destination.

        Returns
        -------
        float
            La distance entre les deux localisations en kilomètres, arrondie à deux décimales.
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

    def transfo_adresse_GPS(self, adresse):
        """Transforme une adresse en coordonnées GPS.

        Parameters
        ----------
        adresse : str
            L'adresse à géocoder.

        Returns
        -------
        tuple or None
            Un tuple contenant la latitude et la longitude de l'adresse si elle est trouvée, sinon None.
        """
        # Convertit l'adresse en chaîne
        address = str(adresse)

        # Crée un géocodeur avec le service Nominatim
        geocoder = Nominatim(user_agent="Mon application Python")

        # Géocode l'adresse pour obtenir les coordonnées GPS
        location = geocoder.geocode(address)

        # Récupère les coordonnées GPS si l'adresse est trouvée
        if location:
            latitude, longitude = location.latitude, location.longitude
            return latitude, longitude
        else:
            print("Adresse non trouvée.")
            return None
