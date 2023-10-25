import requests
import zipfile
from io import BytesIO
import os
from datetime import datetime


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

    return "Le fichier a bien été sauvegardé"
