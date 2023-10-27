import xml.etree.ElementTree as ET
from METIER.Services import Services

tree = ET.parse(r"\\filer-eleves2\id2151\ProjetInfo2A\fichier_xml\stations_service.xml")
root = tree.getroot()

# Créez un ensemble pour stocker temporairement les noms de services
services_set = set()

# Créez une liste pour stocker les objets Services
services_list = []

# Parcourez les éléments 'service' dans le fichier XML
for service_element in root.findall(".//services/service"):
    service_name = service_element.text

    # Vérifiez si le service n'a pas encore été ajouté
    if service_name not in services_set:
        services_set.add(service_name)

        # Créez un objet Services pour le service
        services = Services()
        services.ajouter_service(service_name)

        # Ajoutez l'objet Services à la liste
        services_list.append(services)

# Affichez la liste des objets Services
for service in services_list:
    print(type(service))

from BDD.DAO_Services import Services_Dao
for service in services_list:
    Services_Dao.ajouter_services(service)