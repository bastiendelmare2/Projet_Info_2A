from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.Horaires import Horaires


class Horaires_Dao(metaclass=Singleton):
    def ajouter_horaires(id_horaires, horaires) -> bool:
        """Ajout d'une Station Service dans la BDD

        Parameters
        ----------
         Services: Services

        Returns
        -------
        created : bool
        """


        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.Horaires(id_horaires, horaires) VALUES "
                        "(%(id_horaires)s, %(horaires)s)",
                        {
                            "id_horaires" : id_horaires,
                            "horaires": horaires,
                        },
                    )
                
        except Exception as e:
            print(e)


    def trouver_par_id(self, id) -> Horaires:
        """Touver une Stations Service par id

        Parameters
        ----------
        id : int

        Returns
        -------
        StationsServices : StationsServices

        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet2A.Horaires               "
                        " WHERE id = %(id)s;  ",
                        {"id": Horaires.id},
                    )
        except Exception as e:
            print(e)
            raise

        return Horaires