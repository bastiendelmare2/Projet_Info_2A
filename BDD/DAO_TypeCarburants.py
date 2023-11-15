from BDD.Connexion import DBConnection
from utils.singleton import Singleton


class TypeCarburantDao(metaclass=Singleton):
    def ajouter_TypeCarburant(self, id_typecarburants, nom_type_carburants)-> bool:
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
