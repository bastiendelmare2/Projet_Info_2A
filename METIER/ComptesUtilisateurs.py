import bcrypt


class ComptesUtilisateurs:

    def __init__(self, id_compte, mot_de_passe, identifiant):
        self.id_compte = id_compte
        self.mot_de_passe = mot_de_passe
        self.identifiant = identifiant

    @staticmethod
    def _hash_password(mot_de_passe):
        # Générer un sel aléatoire
        # Hacher le mot de passe avec le sel
        hashed_mot_de_passe = bcrypt.hashpw(mot_de_passe.encode('utf-8'))
        return hashed_mot_de_passe

    def verifier_mot_de_passe(self, mot_de_passe_clair):
        """Vérifie si le mot de passe en clair correspond au hachage stocké."""
        # Hachage du mot de passe clair pour la comparaison
        mot_de_passe_hashe = ComptesUtilisateurs._hash_password(mot_de_passe_clair)
        return mot_de_passe_hashe == self.mot_de_passe

    def modifier_mot_de_passe(self, nouveau_mdp):
        """Modifie le mot de passe pour ce compte."""
        self.mot_de_passe = self._hash_password(nouveau_mdp)

    def __str__(self):
        return f"Compte ID: {self.id_compte}, Identifiant: {self.identifiant}, Mot de passe: {self.mot_de_passe}"