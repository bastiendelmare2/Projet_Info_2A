import xml.etree.ElementTree as ET

tree = ET.parse(r'\\filer-eleves2\id2151\ProjetInfo2A\fichier_xml\stations_service.xml')
root = tree.getroot()

# Supposons que vous avez déjà analysé le fichier XML comme précédemment
# et que vous avez le document XML dans un objet 'root'.
horaires_dict = {}
horaire_id_counter = 1

# Parcourez les éléments 'pdv' dans le fichier XML
for pdv in root.findall('pdv'):
    # Recherchez les éléments 'horaires' sous chaque 'pdv'
    horaires_element = pdv.find('horaires')
    
    if horaires_element is not None:
        # Parcourez les éléments 'jour' sous 'horaires'
        for jour_element in horaires_element.findall('.//jour'):
            jour_id = jour_element.get('id')
            jour_nom = jour_element.get('nom')
            horaire_element = jour_element.find('horaire')
            
            # Vérifiez si 'horaire_element' existe
            if horaire_element is not None:
                ouverture = horaire_element.get('ouverture')
                fermeture = horaire_element.get('fermeture')
            
                # Si le jour n'existe pas déjà dans le dictionnaire, ajoutez-le
                if jour_id not in horaires_dict:
                    horaires_dict[jour_id] = {
                        'nom': jour_nom,
                        'ouverture': ouverture,
                        'fermeture': fermeture,
                        'identifiant': horaire_id_counter
                    }
                    horaire_id_counter += 1

# Maintenant, vous avez un dictionnaire 'horaires_dict' où les clés sont les identifiants de jours
# et les valeurs sont des dictionnaires contenant le nom du jour, les heures d'ouverture et de fermeture
# ainsi que l'identifiant unique pour chaque jour.

# Vous pouvez accéder aux informations des jours comme suit :

for jour_id, info_jour in horaires_dict.items():
    print(f"Identifiant: {info_jour['identifiant']}, Jour: {info_jour['nom']}, Ouverture: {info_jour['ouverture']}, Fermeture: {info_jour['fermeture']}")
