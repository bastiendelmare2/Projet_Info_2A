from BDD.DAO_StationsPreferees import StationsPreferees_Dao
from BDD.DAO_Stations_to_StationsPreferees import StationsToStationsPrefereesDAO

StationsPreferees_Dao.ajouter_StationsPreferee(1 ,5, "test")
StationsToStationsPrefereesDAO.associer_station_a_station_preferee(59780003,1)