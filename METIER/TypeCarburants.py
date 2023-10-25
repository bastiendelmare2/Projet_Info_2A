class TypeCarburants:
    def __init__(self, id_carburant, nom_carburant):
        self.id_carburant = id_carburant
        self.nom_carburant = nom_carburant

    def __str__(self):
        return f"Carburant {self.id_carburant}: {self.nom_carburant}"


# Exemple d'utilisation de la classe
carburant1 = TypeCarburants(1, "Essence")
carburant2 = TypeCarburants(2, "Diesel")

print(carburant1)  # Affiche : Carburant 1: Essence
print(carburant2)  # Affiche : Carburant 2: Diesel