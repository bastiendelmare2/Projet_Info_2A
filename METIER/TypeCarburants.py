class TypeCarburants:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Carburant {self.id_carburant}: {self.nom_carburant}"
