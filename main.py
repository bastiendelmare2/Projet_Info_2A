# On importe les données XML

from BDD.Connexion import DBConnection

with DBConnection().connection as connection:
    req  = """CREATE TABLE Utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    prenom_utilisateur VARCHAR(255) NOT NULL,
    age INT,
    mdp_utilisateur VARCHAR(255) NOT NULL
    );"""
    with connection.cursor() as cursor:
                    cursor.execute(req)



