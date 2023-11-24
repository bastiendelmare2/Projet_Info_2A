from BDD.Connexion import DBConnection
from utils.singleton import Singleton


class TypeCarburantDao(metaclass=Singleton):
    @staticmethod
    def ajouter_TypeCarburant(id_typecarburants, nom_type_carburants)-> bool:
        """Ajout d'un type de carburant dans la BDD

        Parameters
        ----------
        id_typecarburant : int
            Identifiant du type de carburant
        type_carburant : str
            Nom du type de carburant

        Returns
        -------
        created : bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.TypeCarburants(id_typecarburants, nom_type_carburants) VALUES "
                        "(%(id_typecarburants)s, %(nom_type_carburants)s);",
                        {
                            "id_typecarburants": id_typecarburants,
                            "nom_type_carburants": nom_type_carburants,
                        },
                    )
        except Exception as e:
            print(e)

    @staticmethod
    def get_all_type_carburants() -> list:
        """Récupère tous les types de carburant présents dans la table 'TypeCarburants'

        Returns
        -------
        type_carburants_list : list
            Liste des types de carburant présents dans la table
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM projet2a.TypeCarburants;")
                    type_carburants_list = []
                    for carburant_info in cursor.fetchall():
                        carburant_dict = {
                            "id_typecarburants": carburant_info['id_typecarburants'],
                            "nom_type_carburants": carburant_info['nom_type_carburants'],
                        }
                        type_carburants_list.append(carburant_dict)
                    return type_carburants_list
        except Exception as e:
            print(e)