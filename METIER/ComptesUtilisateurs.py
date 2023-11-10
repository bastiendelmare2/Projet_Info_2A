import bcrypt

class ComptesUtilisateurs:
    def __init__(self, id_compte, mot_de_passe, identifiant):
        self.id_compte = id_compte
        self.mot_de_passe = self._hash_password(mot_de_passe)
        self.identifiant = identifiant

    def _hash_password(self, mot_de_passe):
        # Générer un sel aléatoire
        salt = bcrypt.gensalt()
        # Hacher le mot de passe avec le sel
        hashed_mot_de_passe = bcrypt.hashpw(mot_de_passe.encode('utf-8'), salt)
        return hashed_mot_de_passe

