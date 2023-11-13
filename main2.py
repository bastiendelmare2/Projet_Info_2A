from BDD.DAO_StationsPreferees import StationsPreferees_Dao
import pandas as pd

dao = StationsPreferees_Dao()
test = dao.trouver_par_id(5)
print(test)