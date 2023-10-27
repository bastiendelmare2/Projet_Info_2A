#penser à installer pip install geopy
import requests
from geopy.geocoders import Nominatim
import inquirer


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
    print(f"Coordonnées GPS - Latitude : {latitude}, Longitude : {longitude}")

transfo_adresse_GPS("51 rue Blaise Pascal, Bruz")
