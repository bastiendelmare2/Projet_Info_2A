from BDD.Connexion import DBConnection
from utils.singleton import Singleton
from METIER.Horaires import Horaires

class Horaires_Dao(metaclass=Singleton):
    def ajouter_horaires(self, id_horaires, horaires) -> bool:
        """Ajoute des horaires dans la base de données.

        :param id_horaires: Identifiant des horaires.
        :type id_horaires: int
        :param horaires: Horaires à ajouter.
        :type horaires: str
        :return: True si l'ajout a été réalisé avec succès, False sinon.
        :rtype: bool
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.Horaires(id_horaires, horaires) VALUES "
                        "(%(id_horaires)s, %(horaires)s)",
                        {
                            "id_horaires": id_horaires,
                            "horaires": horaires,
                        },
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def trouver_par_id(self, id) -> Horaires:
        """Trouve des horaires par leur identifiant.

        :param id: Identifiant des horaires à trouver.
        :type id: int
        :return: Instance de Horaires correspondante à l'identifiant donné.
        :rtype: Horaires
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM projet2A.Horaires WHERE id = %(id)s;",
                        {"id": id},
                    )
                    horaires_data = cursor.fetchone()
                    if horaires_data:
                        # Crée une instance de Horaires avec les données récupérées de la base de données
                        horaires = Horaires(
                            id_horaires=horaires_data["id_horaires"],
                            horaires=horaires_data["horaires"]
                        )
                        return horaires
                    else:
                        return None
        except Exception as e:
            print(e)
            raise
