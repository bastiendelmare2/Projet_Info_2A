from BDD.Connexion import DBConnection
from utils.singleton import Singleton


class Services_Dao(metaclass=Singleton):
    def ajouter_services(self, id_service, nom_service) -> bool:
        """Ajout d'une Station Service dans la BDD

        Parameters
        ----------
         Services: Services

        Returns
        -------
        created : bool
        """,

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.Services(id_service, nom_service) VALUES "
                        "(%(id_service)s, %(nom_service)s);",
                        {
                            "id_service": id_service,
                            "nom_service": nom_service,
                        },
                    )
        except Exception as e:
            print(e)
