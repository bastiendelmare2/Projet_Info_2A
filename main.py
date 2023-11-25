from API import API
import schedule
import time
import threading

# Variable globale pour vérifier si une tâche est en cours d'exécution
running_task = False

def renouveler_base_periodiquement():
    global running_task
    running_task = True
    print("Importation des données en cours d'exécution...")
    api = API()
    api.renouveler_base_de_donnees()
    running_task = False
    print("Importation terminée.")  

def run_api():
    api = API()
    api.run()

if __name__ == "__main__":
    renouveler_base_periodiquement()

    schedule.every(10).minutes.do(renouveler_base_periodiquement)

    api_thread = threading.Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
