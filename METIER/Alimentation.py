import psycopg2
import sqlite3
import pyodbc


class alimentation:
    # Création base de données utilisateur
    # Utiliser la commande suivante : pip install psycopg2
    def creation_base_donnees(self):
        conn = psycopg2.connect(
            host="localhost:5432",
            database="projet_info",
            user="id2221",
            password="id2221",
        )

        # Créer un curseur
        cursor = conn.cursor()

        # Créer la base de données
        cursor.execute("""CREATE DATABASE my_database
        """)

        # Commiter les modifications
        conn.commit()

        # Fermer la connexion à la base de données
        conn.close()

    def create_table(nom_table="Utilisateurs"):
        # Ouvrir une connexion à la base de données
        ouv_conn = sqlite3.connect(
            host="eleves.domensai.ecole:5432",
            database="id2221",
            user="id2221",
            password="id2221",
            driver="psycopg2-binary",
        )

        # Créer un curseur
        cursor = ouv_conn.cursor()

        # Créer la table
        cursor.execute("""CREATE TABLE {nom_table} (
        id_utilisateur,
        nom_utilisateur,
        prenom_utilisateur,
        age
        );
        """)

        # Commiter les modifications
        ouv_conn.commit()

        # Fermer la connexion à la base de données
        ouv_conn.close()

    def modifier_database():
        # Créer la chaîne de connexion
        connection_string = (
            "DRIVER={SQL Server Native Client 11.0};"
            "SERVER=myserver.example.com;"
            "DATABASE=mydatabase;"
            "UID=myuser;"
            "PWD=mypassword;"
        )

        # Ouvrir la connexion
        conn = pyodbc.connect(connection_string)

        # Commiter les modifications
        conn.commit()

        # Fermer la connexion
        conn.close()

# Questions au prof:
# 1. est ce que les infos renseignées dans la def base de données sont correctes
# 2. Faut il faire une classe a part pour créer une base de données
# 3. Faut il faire plusieurs classes créations bases de données pour données clients
# pour les infos que l'on télécharge