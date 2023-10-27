class ComptesUtilisateurs:
    def __init__(self, id_compte , mot_de_passe, identifiant ):
        self.id_compte = id_compte
        self.mot_de_passe = mot_de_passe
        self.identifiant= identifiant


"Methodes de cette classe a adapter quand les tables seront creer, selon la facon dont les tables sont configurés"

"""def modifier_mdp():
    identifiant_recup= input('Quel est votre identifiant?')
    mdp_atrouver= tableidentifiant['identifiant_recup']
    mdp_donnee= input ('Quel est votre ancien mot de passe?')

    if mdp_atrouver==mdp_donnee:
        nouveau_mdp= input('Quel est le nouveau mot de passe?')
        mdp_a_confirmer= input('Veuillez confirmer le nouveau mot de passe')
        while nouveau_mdp=! mdp_a_confirmer:
            raise ValueError('Les mots de passe ne correspondent pas.')
            else:
                mdp_atrouver= nouveau_mdp #dans la table des utilisateur, l'ancien mdp est remplacé par le nouveai
        else:
            raise ValueError('Les mots de passe ne correspondent pas')
"""


"""def modifierid():
    identifiant_recup= input('Quel est votre identifiant?')
    mdp= tableidentifiant['identifiant_recup']
    mdp_donnee= input ('Quel est votre mot de passe?')

    if mdp==mdp_donnee:
        nouvel_id=input(' Quel est votre nouvel identifiant ?')
        #modifier l'identifiant( depend de la facon dont est configuré la table)
        else:
            raise ValueError('Les mots de passe ne correspondent pas')
"""


 
 
   
"""def creer_compte():
    Cmp= ComptesUtilisateurs()
    id_compte_a_inserer=input(' Quel est votre nouvel identifiant ?')
    mot_de_passe_a_inserer=input(' Quel est votre mot de passe ?')
    identifiant_a_inserer=input(' Quel est votre identifiant ?')
    
    ComptesUtilisateurs.id_compte= id_compte_inserer
    ComptesUtilisateurs.mot_de_passe= mot_de_passe_a_inserer
    ComptesUtilisateurs.id_compte= identifiant_a_inserer

    #puis inserer ces donnees dans la table utilisateurs ( dépend de la facon dont elle est configuré) 

  """  

