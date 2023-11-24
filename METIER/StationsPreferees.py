class StationsPreferees:
    def __init__(self, id_stations_pref, id_compte, nom):
        """Initialise une station préférée avec un identifiant de station, un identifiant de compte et un nom.

        Parameters
        ----------
        id_stations_pref : int
            L'identifiant de la station préférée.
        id_compte : int
            L'identifiant du compte associé à cette station préférée.
        nom : str
            Le nom de la station préférée.

        """
        self.id_stations_pref = id_stations_pref
        self.id_compte = id_compte
        self.nom = nom

    def __str__(self):
        """Renvoie une représentation en chaîne de caractères de la station préférée."""
        return f"Stations Préférées {self.id_stations_pref}"
