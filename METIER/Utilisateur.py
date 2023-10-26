class Utilisateur:
    def __init__(
        self,
        id_utilisateur,
        mdp_utilisateur,
        nom_utilisateur,
        prenom_utilisateur,
        age_utilisateur,
    ):
        self.pseudo_utilisateur = id_utilisateur
        self.mdp_utilisateur = mdp_utilisateur
        self.nom_utilisateur = nom_utilisateur
        self.prenom_utilisateur = prenom_utilisateur
        self.age = age_utilisateur

    def __str__(self):
        return f"Utilisateur {self.id_utilisateur}: {self.prenom_utilisateur} {self.nom_utilisateur}"


# Exemple d'utilisation de la classe Utilisateur avec une liste de stations préférées

