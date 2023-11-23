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
        compte_utilisateur.mot_de_passe = compte_utilisateur._hash_password(compte_utilisateur.mot_de_passe)

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet2a.CompteUtilisateur(id_compte, mot_de_passe, identifiant, sel) VALUES "
                        "(%(id_compte)s, %(mot_de_passe)s, %(identifiant)s, %(sel)s) RETURNING id_compte;",
                        {
                            "id_compte": compte_utilisateur.id_compte,
                            "mot_de_passe": compte_utilisateur.mot_de_passe,
                            "identifiant": compte_utilisateur.identifiant,
                            "sel": compte_utilisateur.sel
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
    def get(id_compte):
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_compte, mot_de_passe, identifiant, sel FROM projet2a.CompteUtilisateur WHERE id_compte = %(id_compte)s;",
                        {"id_compte": id_compte}
                    )
                    compte_data = cursor.fetchone()
                    
                    if compte_data:
                        # Convertir les données récupérées en un objet ComptesUtilisateurs
                        compte = ComptesUtilisateurs(
                            id_compte=compte_data["id_compte"],
                            mot_de_passe=compte_data["mot_de_passe"],
                            identifiant=compte_data["identifiant"],
                            sel=compte_data["sel"],
                            hashed=False  # Le mot de passe n'est pas encore haché dans l'objet ComptesUtilisateurs
                        )
                        return compte
                    else:
                        return None

        except Exception as e:
            print("Erreur lors de la récupération du compte utilisateur :", e)
            return None

    @staticmethod
    def modifier_mot_de_passe(compte_utilisateur: ComptesUtilisateurs, nouveau_mdp: str) -> bool:
        """Modifie le mot de passe d'un compte utilisateur dans la base de données."""
        try:
            # Utilisation directe du mot de passe haché stocké dans l'objet ComptesUtilisateurs
            hashed_password = compte_utilisateur.mot_de_passe

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE projet2a.CompteUtilisateur SET mot_de_passe = %(nouveau_mdp)s WHERE id_compte = %(id_compte)s;",
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
    def supprimer_compte_utilisateur(id_compte: int, identifiant: str) -> bool:
        """Supprime un compte utilisateur de la base de données."""

        # Récupérer les informations du compte utilisateur pour vérification
        compte = Compte_User_DAO.get(id_compte)
        
        if compte:
            # Vérifier seulement l'identifiant
            if compte.identifiant == identifiant:
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "DELETE FROM projet2a.CompteUtilisateur WHERE id_compte = %(id_compte)s;",
                                {"id_compte": id_compte}
                            )
                            connection.commit()
                            return True
                except Exception as e:
                    print(e)
                    return False
            else:
                # Identifiant incorrect
                return False
        else:
            # Compte introuvable
            return False