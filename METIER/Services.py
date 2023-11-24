class Services:
    def __init__(self):
        """Initialise un objet Services avec une liste vide pour stocker les services."""
        self.services = []  # Une liste pour stocker les services

    def ajouter_service(self, service):
        """Ajoute un service à la liste des services.

        Parameters
        ----------
        service : str
            Le service à ajouter.

        """
        self.services.append(service)

    def __str__(self):
        """Renvoie une représentation en chaîne de caractères des services disponibles."""
        return ", ".join(self.services)
