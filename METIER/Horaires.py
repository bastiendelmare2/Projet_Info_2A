class Horaires:
    def __init__(self):
        """Initialise la classe Horaires.

        Cette classe permet de stocker les horaires d'ouverture et de fermeture pour chaque jour.
        Veuillez noter qu'actuellement, la fonctionnalité des horaires n'a pas été implémentée. 
        Cependant, cette classe peut être utilisée comme base pour ajouter ultérieurement cette fonctionnalité.

        """
        self.jours = []  # Une liste pour stocker les horaires de chaque jour

    def ajouter_jour(self, identifiant, nom, ouverture, fermeture):
        """Ajoute les horaires d'ouverture et de fermeture pour un jour spécifique.

        Parameters
        ----------
        identifiant : int
            L'identifiant unique du jour.
        nom : str
            Le nom du jour.
        ouverture : str
            L'heure d'ouverture pour ce jour.
        fermeture : str
            L'heure de fermeture pour ce jour.

        """
        self.jours.append({
            'nom': nom,
            'ouverture': ouverture,
            'fermeture': fermeture
        })
