from SERVICES.Service_compte import ServiceCompte
from SERVICES.Service_stations import Service_Station
from BDD.DAO_StationsServices import StationsServices_Dao

test = StationsServices_Dao()
Service_Station.trouver_stations(test.filtre_stations(), 20,20, 3 )