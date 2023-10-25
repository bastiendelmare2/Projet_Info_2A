import requests
import zipfile
import io
import sqlite3
import xml.etree.ElementTree as ET

# Télécharger et dézipper le fichier
url = "https://donnees.roulez-eco.fr/opendata/instantane"
response = requests.get(url)

if response.status_code == 200:
    zip_content = response.content

    with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
        xml_file_name = "PrixCarburants_instantane.xml"
       
        if xml_file_name in zip_file.namelist():
            xml_content = zip_file.read(xml_file_name).decode("latin-1")
        else:
            print(f"Le fichier {xml_file_name} n'existe pas dans le fichier zip.")
else:
    print("La requête a échoué avec le code de statut :", response.status_code)

# Créer une base de données SQLite
conn = sqlite3.connect('stations.db')

# Créer une table pour stocker les données
c = conn.cursor()
c.execute('''CREATE TABLE stations
            (id INTEGER PRIMARY KEY,
             pdv_id TEXT,
             nom TEXT,
             latitude REAL,
             longitude REAL)''')
 

# Extraire les données du fichier XML et les insérer dans la base de données
root = ET.fromstring(xml_content)

for pdv_element in root.findall(".//pdv"):
    pdv_id = pdv_element.get("id")
    nom = pdv_element.find("adresse").text
    latitude = float(pdv_element.get("latitude"))
    longitude = float(pdv_element.get("longitude"))

    c.execute("INSERT INTO stations (pdv_id, nom, latitude, longitude) VALUES (?, ?, ?, ?)", (pdv_id, nom, latitude, longitude))

conn.commit()
conn.close()