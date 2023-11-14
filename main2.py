from BDD.DAO_StationsServices import StationsServices_Dao

test = StationsServices_Dao.trouver_stations(StationsServices_Dao.filtre_stations(nom_type_carburant= "Gazole"), 25.2, 2.3, n= 5)
print (test)