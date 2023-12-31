import requests
import zipfile
from io import BytesIO
import os
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
from BDD.DAO_Reset_Tables import SuppressionDonnees

class Alimentation:
    @staticmethod
    def lire_fichier_xml(chemin):
        tree = ET.parse(chemin)
        root = tree.getroot()
        stations_service_list = []

        for pdv in root.findall("pdv"):
            identifiant = pdv.get("id")
            adresse = pdv.find("adresse").text
            ville = pdv.find("ville").text
            latitude = pdv.get("latitude")
            longitude = pdv.get("longitude")
            coordonnees = Coordonnees("{:.6e}".format(float(latitude) / 100000), "{:.6e}".format(float(longitude) / 100000))
            carburants = []
            for prix_element in pdv.findall(".//prix"):
                nom = prix_element.get("nom")
                typecarburants = TypeCarburants(nom)
                prix = float(prix_element.get("valeur"))
                carburant = PrixCarburants(type_carburant=typecarburants, prix=prix)
                carburants.append(carburant)
            services = Services()
            for service_element in pdv.find("services").findall("service"):
                service_name = service_element.text
                services.ajouter_service(service_name)
            station_service = StationsServices(
                id_stations=identifiant,
                adresse=adresse,
                ville=ville,
                prixcarburants=carburants,
                coordonnees=coordonnees,
                services=services,
            )
            stations_service_list.append(station_service)

        return stations_service_list

    def XML():
        # URL du fichier à télécharger
        url = "https://donnees.roulez-eco.fr/opendata/instantane"

        # Requête GET à l'API de data.gouv
        response = requests.get(url)

        # Vérification de la réussite de la requête (HTTP status code 200)
        if response.status_code == 200:
            # Extraction du contenu
            zip_content = BytesIO(response.content)

            # Dézipage
            with zipfile.ZipFile(zip_content, "r") as zip_file:
                # Vérification de la présence du document
                # PrixCarburants_instantane.xml à l'intérieur
                if "PrixCarburants_instantane.xml" in zip_file.namelist():
                    # Sauvegarde du fichier
                    xml_content = zip_file.read("PrixCarburants_instantane.xml")

                    # Conversion du fichier (encodage ISO-8859-1)
                    xml_content_str = xml_content.decode("ISO-8859-1")

                    # Réécriture dans le fichier pour qu'il indique le bon encodage final
                    xml_content_str = xml_content_str.replace(
                        '<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>',
                        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                    )
                else:
                    return "Le fichier XML n'est pas présent dans l'archive."
        else:
            return "Erreur de téléchargement du fichier Zip."

        # Répertoire et nom du fichier pour la sauvegarde
        directory_path = "fichier_xml"
        file_name = "stations_service.xml"

        # Création du dossier s'il n'existe pas
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # Chemin du fichier à sauvegarder
        file_path = os.path.join(directory_path, file_name)

        # Écriture
        with open(file_path, "w", encoding="UTF-8") as xml_file:
            xml_file.write(xml_content_str)

        # Chemin du fichier à sauvegarder
        file_path = os.path.join(directory_path, file_name)

        # Écriture
        with open(file_path, "w", encoding="UTF-8") as xml_file:
            xml_file.write(xml_content_str)

        return file_path  # Retourne le chemin du fichier sauvegardé


    @staticmethod
    def alimenter_table_stations_services(stations_service_list):
        for station in stations_service_list:
            StationsServices_Dao.ajouter_StationsServices(station)

    @staticmethod
    def alimenter_table_type_carburant(stations_service_list):
        types_carburants_dict = {}
        next_carburant_id = 1

        for station in stations_service_list:
            for prix_carburant in station.prixcarburants:
                nom_carburant = prix_carburant.type_carburant.nom
                if nom_carburant not in types_carburants_dict:
                    types_carburants_dict[nom_carburant] = next_carburant_id
                    next_carburant_id += 1

        # Ajouter les types de carburants à la table des TypeCarburants
        for nom_typecarburant, id_typecarburant in types_carburants_dict.items():
            TypeCarburantDao.ajouter_TypeCarburant(id_typecarburants=id_typecarburant, nom_type_carburants=nom_typecarburant)

        return types_carburants_dict

    @staticmethod
    def alimenter_table_prix_carburant(stations_service_list, types_carburants_dict):
        prix_carburants_dict = {}

        for station_service in stations_service_list:
            id_station = station_service.id_stations
            for prix_carburant in station_service.prixcarburants:
                nom_carburant = prix_carburant.type_carburant.nom
                id_typecarburant = types_carburants_dict.get(nom_carburant)
                prix = prix_carburant.prix

                if id_typecarburant is not None:
                    key = (id_station, id_typecarburant)
                    prix_carburants_dict[key] = prix

        # Ajouter les prix des carburants à la table des PrixCarburants
        for prix in prix_carburants_dict:
            PrixCarburantsDAO.ajouter_prix_carburant(id_type_carburant=prix[1], id_stations=prix[0], prix=prix_carburants_dict[prix])


    @staticmethod
    def alimenter_table_services(stations_service_list):
        services_dict = {}
        next_service_id = 1

        for station_service in stations_service_list:
            for service_name in station_service.services.services:
                if service_name not in services_dict:
                    services_dict[service_name] = next_service_id
                    next_service_id += 1

        for service in services_dict:
            Services_Dao.ajouter_services(id_service=services_dict[service], nom_service=service)

        return services_dict

    @staticmethod
    def alimenter_table_stations_to_services(stations_service_list, services_dict):
        if services_dict is None:
            # Gérer le cas où services_dict est None (pas correctement initialisé)
            print("Erreur: services_dict est None.")
            return

        stations_to_services_dict = {}

        for station_service in stations_service_list:
            station_id = station_service.id_stations
            service_ids = []

            for service_name in station_service.services.services:
                # Utiliser services_dict.get pour gérer le cas où le service n'est pas dans le dictionnaire
                service_id = services_dict.get(service_name)
                if service_id is not None:
                    service_ids.append(service_id)

            stations_to_services_dict[station_id] = service_ids

        for station_id, service_ids in stations_to_services_dict.items():
            for service_id in service_ids:
                StationsToServicesDAO.associer_station_a_service(id_stations=station_id, id_service=service_id)

    @staticmethod
    def alimenter_table_coordonnees(stations_service_list):
        station_coordinates_dict = {}

        for station in stations_service_list:
            station_id = station.id_stations
            latitude = station.coordonnees.latitude
            longitude = station.coordonnees.longitude

            station_coordinates_dict[station_id] = {"latitude": latitude, "longitude": longitude}

        for station_id, coordinates in station_coordinates_dict.items():
            latitude = round(float(coordinates['latitude']), 6)
            longitude = round(float(coordinates['longitude']), 6)
            Coordonnees_Dao.ajouter_coordonnees(id_stations=station_id, latitude=latitude, longitude=longitude)


    @staticmethod
    def alimenter_table_services_from_xml(chemin):
        tree = ET.parse(chemin)
        root = tree.getroot()

        services_set = set()
        services_list = []

        for service_element in root.findall(".//services/service"):
            service_name = service_element.text

            if service_name not in services_set:
                services_set.add(service_name)

                services = Services()
                services.ajouter_service(service_name)

                services_list.append(services)

        for service in services_list:
            Services_Dao.ajouter_services(service)


    @staticmethod
    def alimenter_toutes_tables(chemin_xml):
        # Lire le fichier XML
        stations_service_list = Alimentation.lire_fichier_xml(chemin_xml)

        # Alimenter la table des StationsServices
        Alimentation.alimenter_table_stations_services(stations_service_list)

        # Alimenter la table des TypeCarburants
        types_carburants_dict = Alimentation.alimenter_table_type_carburant(stations_service_list)

        # Alimenter la table des PrixCarburants
        Alimentation.alimenter_table_prix_carburant(stations_service_list, types_carburants_dict)

        # Alimenter la table des Services
        services_dict = Alimentation.alimenter_table_services(stations_service_list)

        # Alimenter la table des Stations_to_Services
        Alimentation.alimenter_table_stations_to_services(stations_service_list, services_dict)

        # Alimenter la table des Coordonnees
        Alimentation.alimenter_table_coordonnees(stations_service_list)

    def reset_de_la_table():
        SuppressionDonnees.supprimer_donnees_tables()
        chemin = Alimentation.XML()
        Alimentation.alimenter_toutes_tables(chemin)
