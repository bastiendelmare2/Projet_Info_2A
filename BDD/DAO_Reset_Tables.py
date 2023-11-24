from BDD.Connexion import DBConnection
from utils.singleton import Singleton

class SuppressionDonnees(metaclass=Singleton):
    @staticmethod
    def supprimer_donnees_tables():
        # Liste des tables à vider
        tables = [
            "projet2a.Stations_to_Services",
            "projet2a.PrixCarburants",
            "projet2a.Services",
            "projet2a.Horaires",
            "projet2a.Coordonnees",
            "projet2a.StationsServices",
            "projet2a.TypeCarburants"
        ]

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer les données dans les tables sans dépendances
                    for table in tables:
                        cursor.execute(f"DELETE FROM {table};")

        except Exception as e:
            print(e)
