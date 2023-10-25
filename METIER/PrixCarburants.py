class PrixCarburants:
    def __init__(self, type_carburant, prix):
        self.type_carburant = type_carburant
        self.prix = prix

    def __str__(self):
        return f"Prix pour {self.type_carburant}: {self.prix} EUR"