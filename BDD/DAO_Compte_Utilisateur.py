import bcrypt
import binascii
from typing import Optional
from BDD.Connexion import DBConnection
from utils.singleton import Singleton
from METIER.ComptesUtilisateurs import ComptesUtilisateurs


class Compte_User_DAO(metaclass=Singleton):
    @staticmethod
    def ajouter_compte_utilisateur(compte_utilisateur: ComptesUtilisateurs) -> bool:
        """Création d'un compte_utilisateur dans la base de données."""
        res = None
        modif = ComptesUtilisateurs()
        compte_utilisateur.mot_de_passe = modif._hash_password(compte_utilisateur.mot_de_passe)

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Projet2A.compteutilisateur(id_compte, mdp, identifiant) VALUES "
                        "(%(id_compte)s, %(mdp)s, %(identifiant)s) RETURNING id_compte;",
                        {
                            "id_compte": compte_utilisateur.id_compte,
                            "mdp": compte_utilisateur.mot_de_passe,
                            "identifiant": compte_utilisateur.identifiant,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)

        created = False
        if res:
            created = True

        return created

    @staticmethod
    def get(id_compte: int):
        """Récupère un compte utilisateur par son identifiant."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_compte, mdp, identifiant FROM projet2a.compteutilisateur WHERE id_compte = %(id_compte)s;",
                        {"id_compte": id_compte}
                    )
                    res = cursor.fetchone()

                    if res:
                        compte_utilisateur = ComptesUtilisateurs(res['id_compte'], res['mdp'], res['identifiant'])
                        return compte_utilisateur  # Retourne un objet CompteUtilisateurs

                    return None  # Retourne None si aucun compte n'est trouvé avec cet identifiant

        except Exception as e:
            print(e)
            raise ValueError("Une erreur s'est produite lors de la récupération du compte.")


    @staticmethod
    def modifier_mot_de_passe(compte_utilisateur: ComptesUtilisateurs, nouveau_mdp: str) -> bool:
        """Modifie le mot de passe d'un compte utilisateur dans la base de données."""
        try:
            # Utilisation directe du mot de passe haché stocké dans l'objet ComptesUtilisateurs
            hashed_password = compte_utilisateur.mot_de_passe

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE Projet2A.compteutilisateur SET mdp = %(nouveau_mdp)s WHERE id_compte = %(id_compte)s;",
                        {
                            "nouveau_mdp": hashed_password,
                            "id_compte": compte_utilisateur.id_compte
                        }
                    )
                    connection.commit()
                    return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def supprimer_compte_utilisateur(id_compte: int) -> bool:
        """Supprime un compte utilisateur de la base de données."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Projet2A.compteutilisateur WHERE id_compte = %(id_compte)s;",
                        {"id_compte": id_compte}
                    )
                    connection.commit()
                    return True
        except Exception as e:
            print(e)
            return False