import inquirer
import requests
from geopy.geocoders import Nominatim
from transfo_adresse_GPS import transfo_adresse_GPS

class View:
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
        adresse=[
            inquirer.List('recherche',
                              message="Voulez-vous :",
                              choices=["Entrer une adresse postale","Entrer des coordonnées GPS","Revenir à la Page d'acceuil"]
                              ),
        ]
        
        if selected_option == "Entrer une adresse postale":
            adresse=inquirer("Entrer l'adresse postale :")
            coordonnees_GPS=transfo_adresse_GPS(adresse)
            print(coordonnees_GPS)
    
    elif selected_option == "S'authentifier": 
        print("rien")

    elif selected_option == "Créer un compte":
        print("Vous avez sélectionné l'option 3.")
        # Effectuez les actions liées à l'option 3 ici

