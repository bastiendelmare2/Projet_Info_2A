from BDD.DAO_Reset_Tables import SuppressionDonnees
from METIER.Importation import XML
from Alimtentation import Alimentation
from BDD.DAO_StationsServices import StationsServices_Dao


print(StationsServices_Dao.trouver_stations(StationsServices_Dao.filtre_stations("Gazole"), 48.09836111610985, -1.6735038344267077, n = 10, distance_max= 2))