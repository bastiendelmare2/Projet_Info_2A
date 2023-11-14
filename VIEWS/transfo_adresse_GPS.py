# penser à installer pip install geopy
from geopy.geocoders import Nominatim


def transfo_adresse_GPS(adresse):
    # Demandez à l'utilisateur d'entrer une adresse
    adress = str(adresse)

    # Créez un géocodeur avec le service Nominatim
    geocoder = Nominatim(user_agent="Mon application Python")

    # Géocodez l'adresse
    location = geocoder.geocode(adress)

    # Obtenez les coordonnées GPS
    latitude = location.latitude
    longitude = location.longitude

    # Imprimez les coordonnées GPS
    return latitude,longitude

print(transfo_adresse_GPS("51 rue Blaise Pascal, Bruz"))
