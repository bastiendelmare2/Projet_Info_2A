from METIER.Coordonnees import Coordonnees
import json
from datetime import datetime

from BDD.DAO_StationsServices import StationsServices_Dao
final = StationsServices_Dao.filtre_stations(nom_type_carburant= "E10",nom_service= "Laverie")


def add_distance_column(dataframe, ref_latitude, ref_longitude, n):
    start_time = datetime.now()  # Heure d'exécution

    dataframe['distance'] = dataframe.apply(lambda row: Coordonnees.calculer_distance(ref_latitude, ref_longitude, row['latitude'], row['longitude']), axis=1)
    dataframe = dataframe.sort_values(by='distance', ascending=True)
    dataframe = dataframe.sort_values(by='prix', ascending=True)
    dataframe = dataframe.head(n)

    end_time = datetime.now()  # Heure de fin d'exécution

    result_dict = {
        "parameters": {
            "ref_latitude": ref_latitude,
            "ref_longitude": ref_longitude,
            "n": n
        },
        "execution_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "data": dataframe.to_dict(orient='records')
    }

    return result_dict

# Coordonnées du point de référence
ref_latitude = 47.0
ref_longitude = 16.0
n = 5

# Appel de la fonction pour ajouter la colonne "distance" et trier le DataFrame
result = add_distance_column(final, ref_latitude, ref_longitude, n)

# Affichage du résultat au format JSON
print(json.dumps(result, indent=4))  # Conversion en format JSON avec indentation