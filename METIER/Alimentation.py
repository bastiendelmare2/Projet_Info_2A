import psycopg2


class alimentation: 
    #Création base de données utilisateur
    #utiliser la commande suivante : pip install psycopg2

    def creation_base_donnees(self):
        conn = psycopg2.connect(
            host= "eleves.domensai.ecole:5432",
            database="id2221",
            user="id2221",
            password="id2221",
        )

    def connection_base(self):
    # Etape 1 : On récupère une connexion en utilisant la classe DBConnection.
        with DBConnection().connection as connection :
            
    # Etape 2 : à partir de la connexion on fait un curseur pour la requête 
	    with connection.cursor() as cursor : 
    
        # Etape 3 : on exécute notre requête SQL.
    	    	cursor.execute(requete_sql)
    
        # Etape 4 : on stocke le résultat de la requête
    		    res = cursor.fetchall()

    if res:
        # Etape 5 : on agence les résultats selon la forme souhaitée (liste...)
    
    return something
    

#Questions au prof:
#1. est ce que les infos renseignées dans la def base de données sont correctes
#2. Faut il faire une classe a part pour créer une base de données 
#3. Faut il faire plusieurs classes créations bases de données pour données clients 
# pour les infos que l'on télécharge, ...