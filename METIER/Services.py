class Services:
    def __init__(self):
        self.services = []  # Une liste pour stocker les services

    def ajouter_service(self, service):
        self.services.append(service)

    def __str__(self):
        return ", ".join(self.services)
