import xml.etree.ElementTree as ET
from METIER.Services import Services

tree = ET.parse(r'\\filer-eleves2\id2151\ProjetInfo2A\fichier_xml\stations_service.xml')
root = tree.getroot()

# Supposons que vous avez déjà analysé le fichier XML comme précédemment
# et que vous avez le document XML dans un objet 'root'.

# Créez un dictionnaire pour stocker les services et leurs nouveaux identifiants
services_dict = {}
service_id_counter = 1

# Parcourez les éléments 'pdv' dans le fichier XML
for pdv in root.findall('pdv'):
    # Recherchez les éléments 'services' sous chaque 'pdv'
    services_element = pdv.find('services')
    
    # Parcourez les éléments 'service' sous 'services'
    for service_element in services_element.findall('service'):
        service_name = service_element.text
        
        # Si le service n'existe pas déjà dans le dictionnaire, ajoutez-le
        if service_name not in services_dict:
            services_dict[service_name] = service_id_counter
            service_id_counter += 1

# Maintenant, vous avez un dictionnaire 'services_dict' où les clés sont les noms des services
# et les valeurs sont les nouveaux identifiants uniques pour chaque service.

# Vous pouvez accéder aux services et à leurs identifiants comme suit :

for service, service_id in services_dict.items():
    print(f"Service: {service}, Nouvel Identifiant: {service_id}")
