import bcrypt

class ComptesUtilisateurs:
    def __init__(self, id_compte, mot_de_passe, identifiant, sel=None, hashed=False):
        self.id_compte = id_compte
        self.identifiant = identifiant

        if hashed:
            if sel:
                self.sel = sel.encode('utf-8')  # Assigner le sel récupéré depuis la base de données
            else:
                self.sel = bcrypt.gensalt()  # Générer un sel pour le nouveau compte
                self.mot_de_passe = mot_de_passe.encode('utf-8')
        else:
            self.sel = bcrypt.gensalt()  # Générer un sel pour le nouveau compte
            self.mot_de_passe = bcrypt.hashpw(mot_de_passe.encode('utf-8'), self.sel)


    def _hash_password(self, mot_de_passe):
        if not isinstance(mot_de_passe, bytes):
            mot_de_passe = mot_de_passe.encode('utf-8')
        
        if isinstance(self.sel, str):  # Vérifie si le sel est une chaîne de caractères
            self.sel = self.sel.encode('utf-8')  # Assurons-nous que le sel soit encodé

        return bcrypt.hashpw(mot_de_passe, self.sel)

    def get_mot_de_passe_hache(self):
        return self.mot_de_passe  # Cette méthode devrait renvoyer le mot de passe hach

    def verifier_mot_de_passe(self, mot_de_passe_clair):
        """Vérifie si le mot de passe en clair correspond au hachage stocké."""
        if not isinstance(mot_de_passe_clair, bytes):
            mot_de_passe_clair = mot_de_passe_clair.encode('utf-8')
            hashed_password = self._hash_password(mot_de_passe_clair)
        return hashed_password == self.mot_de_passe_hashe

    def modifier_mot_de_passe(self, nouveau_mdp):
        """Modifie le mot de passe pour ce compte."""
        if isinstance(nouveau_mdp, str):
            nouveau_mdp_encoded = nouveau_mdp.encode('utf-8')
        else:
            nouveau_mdp_encoded = nouveau_mdp
        
        self.mot_de_passe_hashe = self._hash_password(nouveau_mdp_encoded)

    def __str__(self):
        return f"ID Compte: {self.id_compte}\nIdentifiant: {self.identifiant}\nMot de passe: {self.mot_de_passe}\nSel: {self.sel}"
