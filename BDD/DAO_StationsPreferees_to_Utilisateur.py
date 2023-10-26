from dao.db_connection import DBConnection
from utils.singleton import Singleton

class StationsPrefereesToUtilisateurDAO(metaclass=Singleton):
    def ajouter_station_preferee(self, id_utilisateur, id_stations_pref) -> bool:
        """Ajouter une station préférée à un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur_id : int
            ID de l'utilisateur
        station_preferee_id : int
            ID de la station préférée

        Returns
        -------
        created : bool
            True si la station préférée a été ajoutée avec succès à l'utilisateur, False sinon
        """
        created = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.StationsPreferees_to_Utilisateur(id_utilisateur, id_stations_pref) VALUES "
                        "(%(id_utilisateur)s, %(id_stations_pref)s);",
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_stations_pref": id_stations_pref,
                        },
                    )
                    created = True
        except Exception as e:
            print(e)

        return created

    def supprimer_station_preferee(self, id_utilisateur, id_stations_pref) -> bool:
        """Supprimer une station préférée d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur_id : int
            ID de l'utilisateur
        station_preferee_id : int
            ID de la station préférée

        Returns
        -------
        deleted : bool
            True si la station préférée a été supprimée avec succès de l'utilisateur, False sinon
        """
        deleted = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Projet2A.StationsPreferees_to_Utilisateur "
                        "WHERE utilisateur_id = %(id_utilisateur)s AND station_preferee_id = %(id_stations_pref)s;",
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_stations_pref": id_stations_pref,
                        },
                    )
                    deleted = True
        except Exception as e:
            print(e)

        return deleted

    def stations_preferees_de_utilisateur(self, id_utilisateur):
        """Trouver les stations préférées d'un utilisateur donné

        Parameters
        ----------
        utilisateur_id : int
            ID de l'utilisateur

        Returns
        -------
        stations_preferees : list
            Liste des ID des stations préférées de l'utilisateur
        """
        stations_preferees = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_stations_pref FROM Projet2A.StationsPreferees_to_Utilisateur WHERE id_utilisateur = %(id_utilisateur)s;",
                        {
                            "id_utilisateur": id_utilisateur,
                        },
                    )
                    stations_preferees = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return stations_preferees

    def utilisateurs_pour_station_preferee(self, id_stations_pref):
        """Trouver les utilisateurs ayant une station préférée donnée

        Parameters
        ----------
        station_preferee_id : int
            ID de la station préférée

        Returns
        -------
        utilisateurs : list
            Liste des ID des utilisateurs ayant la station préférée donnée
        """
        utilisateurs = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT utilisateur_id FROM Projet2A.StationsPreferees_to_Utilisateur WHERE id_stations_pref = %(id_stations_pref)s;",
                        {
                            "station_preferee_id": id_stations_pref,
                        },
                    )
                    utilisateurs = [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)

        return utilisateurs
