class PrixCarburants:
    def __init__(self, type_carburant, prix):
        """Initialise un objet PrixCarburants.

        Parameters
        ----------
        type_carburant : str
            Le type de carburant.
        prix : float
            Le prix du carburant.

        """
        self.type_carburant = type_carburant
        self.prix = prix

    def __str__(self):
        """Renvoie une représentation en chaîne de caractères de l'objet PrixCarburants."""
        return f"Prix pour {self.type_carburant}: {self.prix} EUR"
