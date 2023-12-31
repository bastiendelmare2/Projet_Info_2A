import inquirer
from geopy.geocoders import Nominatim

class Accueil:
    def show(self):
        questions = [
            inquirer.List(
                'menu',
                message="Sélectionnez une option :",
                choices=["Faire une recherche", "S'authentifier", "Créer un compte"],
            ),
        ]

        answers = inquirer.prompt(questions)
        selected_option = answers.get('menu', '').strip().lower()
        return selected_option

class Recherche:
    def transfo_adresse_GPS(self, adresse):
        # Demandez à l'utilisateur d'entrer une adresse
        address = str(adresse)

        # Créez un géocodeur avec le service Nominatim
        geocoder = Nominatim(user_agent="Mon application Python")

        # Géocodez l'adresse
        location = geocoder.geocode(address)

        # Obtenez les coordonnées GPS
        if location:
            latitude, longitude = location.latitude, location.longitude
            return latitude, longitude
        else:
            print("Adresse non trouvée.")
            return None

    def show(self):
        adresse = [
            inquirer.List(
                'recherche',
                message="Voulez-vous :",
                choices=["Entrer une adresse postale", "Entrer des coordonnées GPS", "Revenir à la page d'accueil"]
            ),
        ]

        answers = inquirer.prompt(adresse)
        selected_option_recherche = answers.get('recherche', '').strip().lower()

        if selected_option_recherche == "entrer une adresse postale":
            adresse_postale = input("Entrer l'adresse postale : ").strip()
            coordonnees_GPS = self.transfo_adresse_GPS(adresse_postale)

            if coordonnees_GPS:
                questions_filtres = [
                    inquirer.List(
                        'filtres',
                        message="Voulez-vous appliquer des filtres sur votre recherche ?",
                        choices=["Oui", "Non"],
                    ),
                ]

                answers_filtres = inquirer.prompt(questions_filtres)
                selected_option_filtres = answers_filtres.get('filtres', '').strip().lower()
            
                if selected_option_filtres == "oui":
                    questions_type_carburant = [
                        inquirer.List(
                            'type_carburant',
                            message="Quel carburant souhaitez-vous ? :",
                            choices=["Gazole", "carbu1", "carbu2", "carbu34", "aucun"],
                        ),
                    ]
                    answers_type_carburant = inquirer.prompt(questions_type_carburant)
                    selected_option_type_carburant = answers_type_carburant.get('type_carburant', '').strip().lower()

                    if selected_option_type_carburant == "aucun":
                        filtre_carburant = None
                    
                    else:
                        filtre_carburant = selected_option_type_carburant

                    questions_nb_stations = [
                        inquirer.List(
                            'Nombre de stations affichées',
                            message="Combien de stations souhaitez-vous afficher ? :",
                            choices=["1", "5", "10"],
                        ),
                    ]   

                    answers_nb_stations = inquirer.prompt(questions_nb_stations)
                    selected_option_nb_stations = answers_nb_stations.get('Nombre de stations affichées', '').strip().lower()

                    nb_stations = int(selected_option_nb_stations)
                    distance_max = input("Quelle distance maximum tolérez-vous pour rejoindre la station la plus proche : ")
                    #mettre condition de float

                    print("Voici les stations les plus proches de votre position selon vos critéres")
                    #print(StationsServices_Dao.trouver_stations(StationsServices_Dao.filtre_stations(filtre_carburant), latitude, longitude, nb_stations, distance_max=))
                
                    return selected_option_type_carburant
            
                else:
                    print("Voici les 5 stations les plus proches de votre prosition dans une rayon de 100 kms : ")
                    #print(StationsServices_Dao.trouver_stations(StationsServices_Dao.filtre_stations(None), latitude, longitude, 5, 100))
                
                    return selected_option_filtres
            
            else:
                print("Coordonnées GPS non disponibles.")
                return None
            
        elif selected_option_recherche == "entrer des coordonnées gps":
            latitude = input("Entrer la latitude : ").strip()
            longitude = input("Entrer la longitude : ").strip()
            
            questions_filtres = [
                inquirer.List(
                    'filtres',
                    message="Voulez-vous appliquer des filtres sur votre recherche ?",
                    choices=["Oui", "Non"],
                ),
            ]

            answers_filtres = inquirer.prompt(questions_filtres)
            selected_option_filtres = answers_filtres.get('filtres', '').strip().lower()
            
            if selected_option_filtres == "oui":
                questions_type_carburant = [
                    inquirer.List(
                        'type_carburant',
                        message="Quel carburant souhaitez-vous ? :",
                        choices=["Gazole", "carbu1", "carbu2", "carbu34", "aucun"],
                    ),
                ]
                answers_type_carburant = inquirer.prompt(questions_type_carburant)
                selected_option_type_carburant = answers_type_carburant.get('type_carburant', '').strip().lower()

                if selected_option_type_carburant == "aucun":
                    filtre_carburant = None
                else:
                    filtre_carburant = selected_option_type_carburant

                questions_nb_stations = [
                    inquirer.List(
                        'Nombre de stations affichées',
                        message="Combien de stations souhaitez-vous afficher ? :",
                        choices=["1", "5", "10"],
                    ),
                ]   

                answers_nb_stations = inquirer.prompt(questions_nb_stations)
                selected_option_nb_stations = answers_nb_stations.get('Nombre de stations affichées', '').strip().lower()

                nb_stations = int(selected_option_nb_stations)

                distance_max = input("Quelle distance maximum tolérez-vous pour rejoindre la station la plus proche : ")
                #mettre condition de float
                
                print("Voici les stations les plus proches de votre position selon vos critéres")
                # print(StationsServices_Dao.trouver_stations(StationsServices_Dao.filtre_stations(filtre_carburant), latitude, longitude, nb_stations, distance_max=))
                
                return selected_option_type_carburant
            
            else:

                print("Voici les 5 stations les plus proches de votre prosition dans une rayon de 100 kms : ")
                #print(StationsServices_Dao.trouver_stations(StationsServices_Dao.filtre_stations(None), latitude, longitude, 5, 100))

                return selected_option_filtres

        elif selected_option_recherche == "revenir à la page d'accueil":
            return 'accueil'


class Authentification:
    def __init__(self, utilisateurs):
        self.utilisateurs = utilisateurs
        self.utilisateur_actuel = None

    def authentifier(self):
        while True:
            identifiant = input("Entrer votre identifiant : ").strip()
            mot_de_passe = input("Entrer votre mot de passe : ").strip()

            utilisateur_trouve = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.id_utilisateur == identifiant and utilisateur.mdp_utilisateur == mot_de_passe), None)

            if utilisateur_trouve:
                self.utilisateur_actuel = utilisateur_trouve
                print("Authentification réussie!")

                questions = [
                    inquirer.List(
                        'authentification',
                        message="Voulez-vous:",
                        choices=["Consulter vos listes", "Créer une liste", "Retourner à la page d'accueil"],
                    ),
                ]

                answers = inquirer.prompt(questions)
                selected_option_authentification = answers.get('authentification', '').strip().lower()

                return selected_option_authentification                

            else:
                print("Identifiant ou mot de passe incorrect. Veuillez réessayer.")


class ConsulterListes:
    def show(self):
        #importer les listes de l'utilisateur
        print()
        questions = [
            inquirer.List(
                'Listes_utilisateurs',
                message="Quel liste souhaitez-vous consulter",
                choices=["mettre le nom des listes"],
            ),
        ]

        answers = inquirer.prompt(questions)
        selected_option_listes_utilisateurs = answers.get('Listes_utilisateurs', '').strip().lower()

class CreationCompte:
    def show(self):
        identifiant = input("Entrer votre identifiant : ").strip()
        mot_de_passe = input("Entrer votre mot de passe : ").strip()


class ViewManager:
    def __init__(self):
        self.current_view = Accueil()
        self.utilisateurs = []  # Vous devez initialiser une liste d'utilisateurs ici

    def run(self):
        while True:
            user_input = self.current_view.show()

            if user_input == 'faire une recherche':
                self.current_view = Recherche()
            elif user_input == 'accueil':
                self.current_view = Accueil()
            elif user_input == "s'authentifier":
                auth = Authentification(self.utilisateurs)
                auth.authentifier()
                self.current_view = Accueil()
            elif user_input == 'quitter':
                print("Au revoir!")
                break
            else:
                print("Entrée invalide. Veuillez réessayer.")

if __name__ == "__main__":
    view_manager = ViewManager()
    view_manager.run()
