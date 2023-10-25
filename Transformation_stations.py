import xml.etree.ElementTree as ET
from METIER.Horaires import Horaires
from METIER.Services import Services
from METIER.TypeCarburants import TypeCarburants
from METIER.Coordonnees import Coordonnees
from METIER.StationsServices import StationsServices


tree = ET.parse(r"\\filer-eleves2\id2151\ProjetInfo2A\fichier_xml\stations_service.xml")
root = tree.getroot()
# Créez une liste pour stocker les objets StationService
stations_service_list = []

# Parcourez les éléments 'pdv' dans le fichier XML
for pdv in root.findall("pdv"):
    # Identifiant, adresse et ville
    identifiant = pdv.get("id")
    adresse = pdv.find("adresse").text
    ville = pdv.find("ville").text

    # Coordonnées
    latitude = pdv.get("latitude")
    longitude = pdv.get("longitude")
    coordonnees = Coordonnees(latitude, longitude)

    # Carburants
    carburants = []
    for prix_element in pdv.findall(".//prix"):
        nom = prix_element.get("nom")
        prix = float(prix_element.get("valeur"))
        carburant = TypeCarburants(nom, prix)
        carburants.append(carburant)

    # Horaires
    horaires = Horaires()
    for jour_element in pdv.findall(".//jour"):
        nom = jour_element.get("nom")
        horaire_element = jour_element.find("horaire")
        if horaire_element is not None:
            ouverture = horaire_element.get("ouverture")
            fermeture = horaire_element.get("fermeture")
            horaires.ajouter_jour(identifiant, nom, ouverture, fermeture)

    # Services
    services = Services()
    for service_element in pdv.find("services").findall("service"):
        service_name = service_element.text
        services.ajouter_service(service_name)

    # Créez un objet StationService
    station_service = StationsServices(
        id_stations=identifiant,
        adresse=adresse,
        ville=ville,
        typecarburants=carburants,
        horaires=horaires,
        coordonnees=coordonnees,
        services=services,
    )

    # Ajoutez l'objet à la liste
    stations_service_list.append(station_service)


for station in stations_service_list:
    print(station)
