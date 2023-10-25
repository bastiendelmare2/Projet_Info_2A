import xml.etree.ElementTree as ET
from METIER.StationsServices import StationsServices

tree = ET.parse(r'\\filer-eleves2\id2151\ProjetInfo2A\fichier_xml\stations_service.xml')
root = tree.getroot()
# Créer une liste pour stocker les objets "stations-service"
liste_stations_service = []

# Parcourir les éléments "pdv" dans le XML
for pdv in root.findall('pdv'):
    id = pdv.get('id')
    adresse = pdv.find('adresse').text
    ville = pdv.find('ville').text

    # Créer un objet "station-service" avec les attributs souhaités
    station_service = StationsServices(id, adresse, ville)

    # Ajouter l'objet à la liste
    liste_stations_service.append(station_service)

# Afficher la liste des stations-service
for station_service in liste_stations_service:
    print(station_service)