class TypeCarburants:
    def __init__(self, nom):
        """
        Initialise une instance de TypeCarburants.

        Parameters
        ----------
        nom : str
            Nom du type de carburant.

        Attributes
        ----------
        nom : str
            Nom du type de carburant.
        """
        self.nom = nom

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du type de carburant.

        Returns
        -------
        str
            Chaîne représentant le nom du type de carburant.
        """
        return self.nom  # Renvoie le nom du type de carburant lors de l'impression
