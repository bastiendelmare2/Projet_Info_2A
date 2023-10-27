from BDD.Connexion import DBConnection
from utils.singleton import Singleton

from METIER.Horaires import Horaires


class Services_Dao(metaclass=Singleton):
    def Services(self, Horaires: Horaires) -> bool:
        """Ajout d'une Station Service dans la BDD

        Parameters
        ----------
         Services: Services

        Returns
        -------
        created : bool
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.Horaires(horaires) VALUES "
                        "(%(horaires)s)",
                        {
                            "horaires": Horaires.horaires,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

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
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise

        return Horaires