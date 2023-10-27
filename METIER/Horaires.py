class Horaires:
    def __init__(self):
        self.jours = []  # Une liste pour stocker les horaires de chaque jour

    def ajouter_jour(self, identifiant, nom, ouverture, fermeture):
        self.jours.append({
            'nom': nom,
            'ouverture': ouverture,
            'fermeture': fermeture
        })