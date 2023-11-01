import xml.etree.ElementTree as ET
from METIER.Horaires import Horaires
from METIER.Services import Services
from METIER.TypeCarburants import TypeCarburants
from METIER.PrixCarburants import PrixCarburants
from METIER.Coordonnees import Coordonnees
from METIER.StationsServices import StationsServices

from BDD.DAO_StationsServices import StationsServices_Dao
from BDD.DAO_TypeCarburants import TypeCarburantDao
from BDD.DAO_PrixCarburants import PrixCarburantsDAO
from BDD.DAO_Services import Services_Dao
from BDD.DAO_Stations_to_Services import StationsToServicesDAO
from BDD.DAO_Coordonnees import Coordonnees_Dao
from BDD.DAO_Horaires  import Horaires_Dao



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
        typecarburants = TypeCarburants(nom)
        prix = float(prix_element.get("valeur"))
        carburant = PrixCarburants(type_carburant=typecarburants, prix=prix)
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
        prixcarburants=carburants,
        horaires=horaires,
        coordonnees=coordonnees,
        services=services,
    )

    # Ajoutez l'objet à la liste
    stations_service_list.append(station_service)

#for stations in stations_service_list:
#    print(stations)

# Alimenter la table Stations Services
#for station in stations_service_list:
#    StationsServices_Dao.ajouter_StationsServices(station)
   

# Affichez la liste des stations services avec uniquement l'identifiant, l'adresse et la ville
#for station_info in stations_service_info_list:
#   print(f"ID : {station_info['identifiant']}, Adresse : {station_info['adresse']}, Ville : {station_info['ville']}")


# On alimente la table TypeCarburant
# Créez un dictionnaire pour stocker les types de carburant avec des identifiants uniques
types_carburants_dict = {}
next_carburant_id = 1

# Parcourez les objets StationsServices
for station in stations_service_list:
    for prix_carburant in station.prixcarburants:
        nom_carburant = prix_carburant.type_carburant.nom
        if nom_carburant not in types_carburants_dict:
            # Si le type de carburant n'existe pas dans le dictionnaire, créez-le et associez-lui un identifiant unique
            types_carburants_dict[nom_carburant] = next_carburant_id
            next_carburant_id += 1


# Convertissez le dictionnaire en une liste
#for i in types_carburants_dict:
#    TypeCarburantDao.ajouter_TypeCarburant(id_typecarburants = types_carburants_dict[i], nom_type_carburants= i )

# Créez un dictionnaire pour stocker les données souhaitées
# Créez un dictionnaire pour stocker les données souhaitées
prix_carburants_dict = {}

# Parcourez la liste de StationsServices
for station_service in stations_service_list:
    # Récupérez l'identifiant de la station
    id_station = station_service.id_stations

    # Parcourez les prix des carburants pour cette station
    for prix_carburant in station_service.prixcarburants:
        # Récupérez le nom du carburant
        nom_carburant = prix_carburant.type_carburant.nom

        # Récupérez l'identifiant du type de carburant à partir du dictionnaire
        id_typecarburant = types_carburants_dict.get(nom_carburant)

        # Récupérez le prix du carburant
        prix = prix_carburant.prix

        if id_typecarburant is not None:
            # Associez les données dans le dictionnaire avec une liste en tant que clé
            key = (id_station, id_typecarburant)

            # Associez le prix au type de carburant dans le dictionnaire
            prix_carburants_dict[key] = prix

#for prix in prix_carburants_dict:
#    PrixCarburantsDAO.ajouter_prix_carburant(id_type_carburant= prix[1], id_stations = prix[0], prix= prix_carburants_dict[prix])


# TABLE SERVICE
# Un dictionnaire pour stocker les correspondances entre le nom du service et son identifiant
services_dict = {}

# L'identifiant unique initial pour les services
next_service_id = 1

for station_service in stations_service_list:
    for service_name in station_service.services.services:
        if service_name not in services_dict:
            # Si le service n'existe pas dans le dictionnaire, créez-le et associez-lui un identifiant unique
            services_dict[service_name] = next_service_id
            next_service_id += 1

# À ce stade, le dictionnaire services_dict associe chaque nom de service à un identifiant unique

print(services_dict)
#for service in services_dict:
#   Services_Dao.ajouter_services(id_service= services_dict[service], nom_service = service)

# Un dictionnaire pour stocker les correspondances entre l'identifiant de la station et l'identifiant du service associé
stations_to_services_dict = {}

for station_service in stations_service_list:
    station_id = station_service.id_stations
    service_ids = []  # Liste pour stocker les identifiants des services associés

    for service_name in station_service.services.services:
        if service_name in services_dict:
            # Si le service existe dans le dictionnaire services_dict, récupérez son identifiant
            service_id = services_dict[service_name]
            service_ids.append(service_id)

    # Associez l'identifiant de la station aux identifiants des services associés
    stations_to_services_dict[station_id] = service_ids

# À ce stade, le dictionnaire stations_to_services_dict associe l'identifiant de chaque station à la liste des identifiants de services associés


#for station_id, service_ids in stations_to_services_dict.items():
 #    for service_id in service_ids:
      # Appelez la méthode associer_station_a_station_preferee pour chaque paire (station, service)
#        StationsToServicesDAO.associer_station_a_service(id_stations= station_id, id_service= service_id)


# Créez un dictionnaire pour stocker les informations de latitude et de longitude pour chaque station
station_coordinates_dict = {}

# Itérez sur la liste des objets StationsServices
for station in stations_service_list:
    station_id = station.id_stations  # Identifiant de la station
    latitude = station.coordonnees.latitude  # Latitude de la station
    longitude = station.coordonnees.longitude  # Longitude de la station

    # Ajoutez ces informations au dictionnaire
    station_coordinates_dict[station_id] = {"latitude": latitude, "longitude": longitude}

# Affichez le dictionnaire

#for station_id, coordinates in station_coordinates_dict.items():
 #   latitude = round(float(coordinates['latitude']),1)
  #  longitude = round(float(coordinates['longitude']),1)

    # Utilisez la méthode ajouter_coordonnees pour ajouter les coordonnées à la BDD
   # Coordonnees_Dao.ajouter_coordonnees(id_stations=station_id, latitude=latitude, longitude=longitude)


next_horaire_id = 1  # Variable pour générer des identifiants uniques pour les horaires
horaires_dict = {}  # Dictionnaire pour stocker les correspondances entre les identifiants et les horaires

for station_service in stations_service_list:
    for horaire in station_service.horaires.jours:
        horaire_name = f"{horaire['nom']} ({horaire['ouverture']} - {horaire['fermeture']})"
        if horaire_name not in horaires_dict:
            # Si l'horaire n'existe pas dans le dictionnaire, créez-le et associez-lui un identifiant unique
            horaires_dict[next_horaire_id] = horaire_name
            next_horaire_id += 1

# À ce stade, le dictionnaire horaires_dict associe chaque identifiant unique à un horaire
#print(horaires_dict)

#for h in horaires_dict:
    #Horaires_Dao.ajouter_horaires(h, horaires_dict[h])+

# Un dictionnaire pour stocker les correspondances entre l'identifiant de la station et les horaires associés

