#Avant il faut faire pip install inquirer
import inquirer
import requests



def accueil():
    print("accueil")
    """Pour intégrargir avec le client"""    
    questions = [
        inquirer.List('menu',
                    message="Sélectionnez une option :",
                    choices=["Faire une recherche","S'authentifier", "Créer un compte"],
                    ),
    ]

    answers = inquirer.prompt(questions)
    selected_option = answers['menu']

    if selected_option == "Faire une recherche":
        faire_une_recherche()

    elif selected_option == "S'authentifier":
        authentifier()

    elif selected_option == "Créer un compte":
        creation_compte()


def faire_une_recherche():
    adresse=[
        inquirer.List('recherche',
                        message="Voulez-vous :",
                        choices=["Entrer une adresse postale","Entrer des coordonnées GPS","Revenir à la page d'accueil"]
                        ),
    ]

    answers = inquirer.prompt(adresse)
    selected_option_recherche = answers['recherche']

    if selected_option_recherche == "Entrer une adresse postale":
        adresse_postale=input("Entrer l'adresse postale :")
        coordonnees_GPS=transfo_adresse_GPS(adresse_postale)            

    elif selected_option_recherche == "Entrer des coordonnées GPS":
        latitude=input("Entrer la latitude : ")
        longitude=input("Entrer la longitude : ")

    elif selected_option_recherche == "Revenir à la page d'accueil":
        print("rien")