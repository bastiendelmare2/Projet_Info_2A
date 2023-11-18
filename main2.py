from SERVICES.Service_stations import Service_Station
from BDD.DAO_StationsServices import StationsServices_Dao


print(Service_Station.trouver_stations(StationsServices_Dao.filtre_stations(),48.08869586050125, -1.719080231856629, 3))