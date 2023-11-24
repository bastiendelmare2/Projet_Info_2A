from BDD.Connexion import DBConnection
from utils.singleton import Singleton

class Services_Dao(metaclass=Singleton):
    @staticmethod
    def ajouter_services(id_service, nom_service) -> bool:
        """Ajoute un service dans la base de données.

        :param id_service: Identifiant du service.
        :type id_service: int
        :param nom_service: Nom du service.
        :type nom_service: str
        :return: True si l'ajout a été réalisé avec succès, False sinon.
        :rtype: bool
        """
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
                    return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get(id_service) -> dict:
        """Récupère les informations d'un service à partir de son ID.

        :param id_service: Identifiant du service à récupérer.
        :type id_service: int
        :return: Informations du service sous forme de dictionnaire si trouvé, sinon None.
        :rtype: dict or None
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM projet2a.Services WHERE id_service = %(id_service)s;",
                        {"id_service": id_service},
                    )
                    service_info = cursor.fetchone()
                    if service_info:
                        # Mapping des résultats de la requête dans un dictionnaire
                        service_dict = {
                            "id_service": service_info[0],
                            "nom_service": service_info[1],
                            # Ajoutez d'autres colonnes de la table si nécessaire
                        }
                        return service_dict
                    else:
                        return None
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_all_services() -> list:
        """Récupère tous les services présents dans la table 'Services'.

        :return: Liste des services présents dans la table.
        :rtype: list[dict]
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM projet2a.Services;")
                    services_list = []
                    for service_info in cursor.fetchall():
                        service_dict = {
                            "id_service": service_info['id_service'],
                            "nom_service": service_info['nom_service'],
                            # Ajoutez d'autres colonnes de la table si nécessaire
                        }
                        services_list.append(service_dict)
                    return services_list
        except Exception as e:
            print(e)
            return []
