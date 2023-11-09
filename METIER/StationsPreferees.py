# Import des classes
class StationsPreferees:
    def __init__(self, id_stations_pref, id_compte):
        self.id_stations_pref = id_stations_pref
        self.id_compte = id_compte

    def __str__(self):
        return f"Stations Préférées {self.id_stations_pref}"

        