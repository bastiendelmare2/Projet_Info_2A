class Horaires:
    def __init__(self, id_horaire, plage_horaire):
        self.id_horaire = id_horaire
        self.plage_horaire = plage_horaire

    def __str__(self):
        return f"Horaire {self.id_horaire}: {self.plage_horaire}"


# Exemple d'utilisation de la classe
horaire1 = Horaires(1, ("Lundi, 10:00 - 12:00"))
horaire2 = Horaires(2, ("Mardi, 14:00 - 16:00"))

print(horaire1)  # Affiche : Horaire 1: Lundi, 10:00 - 12:00
print(horaire2)  # Affiche : Horaire 2: Mardi, 14:00 - 16:00