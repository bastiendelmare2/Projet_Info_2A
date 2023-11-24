from API import API
import schedule
import time
import threading

def renouveler_base_periodiquement():
    api = API()
    api.renouveler_base_de_donnees()

def run_api():
    api = API()
    api.run()

if __name__ == "__main__":
    # Renouveler la base de données au démarrage
    renouveler_base_periodiquement()

    # Planifier le renouvellement toutes les 10 minutes après le démarrage initial
    schedule.every(10).minutes.do(renouveler_base_periodiquement)

    # Démarrer un thread pour exécuter l'API
    api_thread = threading.Thread(target=run_api)
    api_thread.start()

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)  # Attente pour réduire la charge du processeur
    except KeyboardInterrupt:
        pass  # Permet de sortir proprement de la boucle sur Ctrl+C sans afficher d'erreur
