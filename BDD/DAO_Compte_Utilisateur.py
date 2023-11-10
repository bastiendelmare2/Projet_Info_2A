import bcrypt
import binascii
from BDD.Connexion import DBConnection
from utils.singleton import Singleton
from METIER.ComptesUtilisateurs import ComptesUtilisateurs

class Compte_User_DAO(metaclass=Singleton):
    @staticmethod
    def ajouter_compte_utilisateur(compte_utilisateur: ComptesUtilisateurs) -> bool:
        """Création d'un compte_utilisateur dans la base de données."""
        res = None

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
    def verifier_connexion(identifiant: str, mot_de_passe: str) -> bool:
        """Vérification des informations de connexion d'un utilisateur."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Récupérer le mot de passe haché depuis la base de données
                    cursor.execute(
                        "SELECT mdp FROM Projet2A.compteutilisateur WHERE identifiant = %(identifiant)s;",
                        {"identifiant": identifiant},
                    )
                    hashed_password = cursor.fetchone()

                    # Vérifier si le mot de passe entré correspond au mot de passe stocké
                    if hashed_password:
                        hashed_password_str = hashed_password['mdp']

                        # Convertir le format hexadécimal en une chaîne binaire
                        hashed_password_bin = binascii.unhexlify(hashed_password_str[2:]) 

                        return bcrypt.checkpw(mot_de_passe.encode('utf-8'), hashed_password_bin)
        except Exception as e:
            print(e)

        return False






