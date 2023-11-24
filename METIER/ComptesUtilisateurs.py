import bcrypt

class ComptesUtilisateurs:
    def __init__(self, id_compte, mot_de_passe, identifiant, sel=None, hashed=False):
        """Initialise un objet de compte utilisateur.

        Parameters
        ----------
        id_compte : int
            Identifiant du compte utilisateur.
        mot_de_passe : str
            Mot de passe pour le compte utilisateur.
        identifiant : str
            Identifiant unique pour le compte utilisateur.
        sel : str, optional
            Sel utilisé pour le hachage du mot de passe. S'il n'est pas fourni, un sel est généré.
        hashed : bool, optional
            Booléen indiquant si le mot de passe est déjà haché. Par défaut, False.

        Raises
        ------
        ValueError
            Si le mot de passe n'est pas fourni ou si le sel n'est pas une chaîne de caractères.

        Notes
        -----
        Si le mot de passe est déjà haché, le sel doit être récupéré depuis la base de données.
        Sinon, un sel est généré pour le nouveau compte.

        """
        self.id_compte = id_compte
        self.identifiant = identifiant

        if hashed:
            if sel:
                self.sel = sel.encode('utf-8')  
            else:
                self.sel = bcrypt.gensalt()
                self.mot_de_passe = mot_de_passe.encode('utf-8')
        else:
            self.sel = bcrypt.gensalt()  
            self.mot_de_passe = bcrypt.hashpw(mot_de_passe.encode('utf-8'), self.sel)

    def _hash_password(self, mot_de_passe):
        """Hache le mot de passe avec le sel associé.

        Parameters
        ----------
        mot_de_passe : str
            Mot de passe à hacher.

        Returns
        -------
        bytes
            Mot de passe haché.

        """
        if not isinstance(mot_de_passe, bytes):
            mot_de_passe = mot_de_passe.encode('utf-8')
        
        if isinstance(self.sel, str):  
            self.sel = self.sel.encode('utf-8')  

        return bcrypt.hashpw(mot_de_passe, self.sel)

    def get_mot_de_passe_hache(self):
        """Récupère le mot de passe haché.

        Returns
        -------
        bytes
            Mot de passe haché.

        """
        return self.mot_de_passe  

    def verifier_mot_de_passe(self, mot_de_passe_clair):
        """Vérifie si le mot de passe en clair correspond au mot de passe haché stocké.

        Parameters
        ----------
        mot_de_passe_clair : str
            Mot de passe en clair à vérifier.

        Returns
        -------
        bool
            True si le mot de passe en clair correspond au mot de passe haché stocké, sinon False.

        """
        if not isinstance(mot_de_passe_clair, bytes):
            mot_de_passe_clair = mot_de_passe_clair.encode('utf-8')
        hashed_password = self._hash_password(mot_de_passe_clair)
        return hashed_password == self.mot_de_passe

    def modifier_mot_de_passe(self, nouveau_mdp):
        """Modifie le mot de passe pour ce compte.

        Parameters
        ----------
        nouveau_mdp : str
            Nouveau mot de passe.

        """
        if isinstance(nouveau_mdp, str):
            nouveau_mdp_encoded = nouveau_mdp.encode('utf-8')
        else:
            nouveau_mdp_encoded = nouveau_mdp
        
        self.mot_de_passe = self._hash_password(nouveau_mdp_encoded)

    def __str__(self):
        """Renvoie une représentation en chaîne de caractères des attributs de l'objet compte.

        Returns
        -------
        str
            Représentation en chaîne de caractères.

        """
        return f"ID Compte: {self.id_compte}\nIdentifiant: {self.identifiant}\nMot de passe: {self.mot_de_passe}\nSel: {self.sel}"
