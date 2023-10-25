import xml.etree.ElementTree as ET
from METIER.Services import Services

tree = ET.parse(r'\\filer-eleves2\id2151\ProjetInfo2A\fichier_xml\stations_service.xml')
root = tree.getroot()

# Supposons que vous avez déjà analysé le fichier XML comme précédemment
# et que vous avez le document XML dans un objet 'root'.

# Créez un dictionnaire pour stocker les services et leurs identifiants
services_dict = {}

# Parcourez les éléments 'pdv' dans le fichier XML
for pdv in root.findall('pdv'):
    # Recherchez les éléments 'services' sous chaque 'pdv'
    services_element = pdv.find('services')
    
    # Parcourez les éléments 'service' sous 'services'
    for service_element in services_element.findall('service'):
        service_name = service_element.text
        service_id = pdv.get('id')
        
        # Si le service n'existe pas déjà dans le dictionnaire, ajoutez-le
        if service_name not in services_dict:
            services_dict[service_name] = []
        
        # Ajoutez l'identifiant du 'pdv' au service correspondant
        services_dict[service_name].append(service_id)

# Maintenant, vous avez un dictionnaire 'services_dict' où les clés sont les noms des services
# et les valeurs sont les listes d'identifiants correspondants

# Vous pouvez accéder aux services et à leurs identifiants comme suit :

for service, ids in services_dict.items():
    print(f"Service: {service}, Identifiants: {', '.join(ids)}")
